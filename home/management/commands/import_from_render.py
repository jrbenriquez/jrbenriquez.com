"""
One-off import of the Render (Postgres) content into a fresh SQLite database.

Make the dump on your own machine (never paste the DB URL anywhere):

    DATABASE_URL="$RENDER_DB_URL" python manage.py dumpdata \\
      --natural-foreign \\
      -e contenttypes -e auth.permission -e sessions -e admin.logentry \\
      -e wagtailcore.pagelogentry -e wagtailcore.modellogentry \\
      -e wagtailcore.referenceindex -e wagtailsearch \\
      -e wagtailcore.workflowstate -e wagtailcore.taskstate \\
      > render_dump.json

Then on the new database, after `migrate`:

    python manage.py import_from_render render_dump.json

`migrate` creates a default "Home" page, a `localhost` Site (home migration
0002) and the default Editors/Moderators groups. Those collide with the imported
data, so they are removed first.
Refuses to run if the database already holds real content (use --force to
override). Rebuilds the search index afterwards.
"""

from django.contrib.auth.models import Group
from django.core.management import call_command
from django.core.management.base import BaseCommand, CommandError
from django.db import transaction

from blog.models import BlogPostPage
from wagtail.models import Page, Site


class Command(BaseCommand):
    help = "Replace the migration-default Home page and Site with a dumpdata file."

    def add_arguments(self, parser):
        parser.add_argument("dump_file")
        parser.add_argument("--force", action="store_true", help="Run even if content already exists.")

    def handle(self, *args, dump_file, force, **options):
        # Fresh DB after migrate: Root (depth 1) + default Home (depth 2) only.
        if not force and (Page.objects.filter(depth__gt=2).exists() or BlogPostPage.objects.exists()):
            raise CommandError("Database already has content. Use --force only if you mean to replace it.")

        with transaction.atomic():
            Site.objects.all().delete()
            Group.objects.all().delete()  # default Editors/Moderators; dump brings its own
            Page.objects.filter(depth__gt=1).delete()
            call_command("loaddata", dump_file, verbosity=1)

        call_command("update_index")

        self.stdout.write(self.style.SUCCESS(
            f"Imported. Pages: {Page.objects.count()}, blog posts: {BlogPostPage.objects.count()}, "
            f"sites: {list(Site.objects.values_list('hostname', flat=True))}"
        ))
