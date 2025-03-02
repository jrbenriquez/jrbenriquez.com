#!/usr/bin/env bash
# Exit on error
set -o errexit

# Convert static asset files
poetry run python manage.py collectstatic --no-input

# Apply any outstanding database migrations
poetry run python manage.py migrate
