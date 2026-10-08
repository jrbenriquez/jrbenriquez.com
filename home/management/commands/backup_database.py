"""
Consistent backup of the SQLite database, with retention pruning and an
optional offsite copy to the R2/S3 bucket.

Do not `cp` the live DB: it runs in WAL mode, so the data is spread over
db.sqlite3, -wal and -shm and a plain copy can be torn. This uses sqlite's
online backup API (a consistent snapshot while the app keeps writing) and
verifies the result with PRAGMA integrity_check before reporting success.
Restoring is just putting the snapshot file back as db.sqlite3.

Usage:
    python manage.py backup_database
    python manage.py backup_database --upload        # also copy to R2 under backups/
    python manage.py backup_database --output-dir /app/backups --retain-days 7 --keep 7

Offsite upload is opt-in because the bucket also holds public media and the
snapshot contains user password hashes.
"""

import datetime
import sqlite3
from pathlib import Path

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from django.db import connection
from django.utils import timezone

PREFIX = "jrbenriquez-"
REMOTE_PREFIX = "backups/"


class Command(BaseCommand):
    help = "Back up the SQLite database and prune old backups."

    def add_arguments(self, parser):
        parser.add_argument("--output-dir", default=None, help="Default: <BASE_DIR>/backups.")
        parser.add_argument("--retain-days", type=int, default=7)
        parser.add_argument("--keep", type=int, default=7, help="Always keep at least this many.")
        parser.add_argument("--upload", action="store_true", help="Also copy to the R2 bucket.")

    def handle(self, *args, output_dir, retain_days, keep, upload, **options):
        if connection.vendor != "sqlite":
            raise CommandError(f"SQLite only; the database is {connection.vendor}. Use pg_dump.")

        out = Path(output_dir) if output_dir else Path(settings.BASE_DIR) / "backups"
        out.mkdir(parents=True, exist_ok=True)
        snapshot = out / f"{PREFIX}{timezone.now():%Y%m%dT%H%M%SZ}.sqlite3"

        self.stdout.write(f"Backing up {connection.settings_dict['NAME']} -> {snapshot}")
        self._snapshot(snapshot)
        self._verify(snapshot)
        self.stdout.write(self.style.SUCCESS(
            f"Backup written: {snapshot} ({snapshot.stat().st_size / 1024:.1f} KiB)"))

        self._prune_local(out, retain_days, keep)
        if upload:
            self._upload(snapshot, retain_days, keep)

    def _snapshot(self, dest):
        connection.ensure_connection()
        target = sqlite3.connect(dest)
        try:
            connection.connection.backup(target)
        except Exception as exc:
            dest.unlink(missing_ok=True)
            raise CommandError(f"Backup failed: {exc}") from exc
        finally:
            target.close()

    def _verify(self, snapshot):
        check = sqlite3.connect(snapshot)
        try:
            result = check.execute("PRAGMA integrity_check").fetchone()[0]
        finally:
            check.close()
        if result != "ok":
            snapshot.unlink(missing_ok=True)
            raise CommandError(f"Snapshot failed integrity_check ({result}); discarded.")
        self.stdout.write("Snapshot verified (integrity_check: ok)")

    def _prune_local(self, out, retain_days, keep):
        files = sorted(p for p in out.glob(f"{PREFIX}*.sqlite3") if p.is_file())
        survivors = set(files[-keep:]) if keep > 0 else set()
        cutoff = timezone.now() - datetime.timedelta(days=retain_days)
        pruned = 0
        for p in files:
            modified = datetime.datetime.fromtimestamp(p.stat().st_mtime, tz=datetime.timezone.utc)
            if p not in survivors and modified < cutoff:
                p.unlink(missing_ok=True)
                pruned += 1
        self.stdout.write(f"Retention: {len(files) - pruned} kept, {pruned} pruned")

    def _upload(self, snapshot, retain_days, keep):
        import boto3

        bucket = settings.AWS_STORAGE_BUCKET_NAME
        if not bucket:
            raise CommandError("--upload needs AWS_STORAGE_BUCKET_NAME (and R2 credentials) set.")
        client = boto3.client(
            "s3",
            aws_access_key_id=settings.AWS_S3_ACCESS_KEY_ID or None,
            aws_secret_access_key=settings.AWS_S3_SECRET_ACCESS_KEY or None,
            endpoint_url=settings.AWS_S3_ENDPOINT_URL or None,
            region_name="auto",
        )
        key = f"{REMOTE_PREFIX}{snapshot.name}"
        try:
            client.upload_file(str(snapshot), bucket, key)
        except Exception as exc:
            # The local snapshot is valid; a failed offsite copy is a warning, not a failed backup.
            self.stdout.write(self.style.WARNING(f"Offsite upload failed: {exc}. Local backup is fine."))
            return
        self.stdout.write(self.style.SUCCESS(f"Uploaded to {bucket}/{key}"))

        objs = []
        for page in client.get_paginator("list_objects_v2").paginate(Bucket=bucket, Prefix=f"{REMOTE_PREFIX}{PREFIX}"):
            objs += [(o["Key"], o["LastModified"]) for o in page.get("Contents", []) if o["Key"].endswith(".sqlite3")]
        objs.sort(key=lambda o: o[1])
        survivors = {k for k, _ in objs[-keep:]} if keep > 0 else set()
        cutoff = timezone.now() - datetime.timedelta(days=retain_days)
        stale = [k for k, m in objs if k not in survivors and m < cutoff]
        for i in range(0, len(stale), 1000):
            client.delete_objects(Bucket=bucket, Delete={"Objects": [{"Key": k} for k in stale[i:i + 1000]]})
        if stale:
            self.stdout.write(f"Pruned {len(stale)} remote backup(s)")
