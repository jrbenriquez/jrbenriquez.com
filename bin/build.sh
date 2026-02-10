#!/usr/bin/env bash
# Exit on error
set -o errexit

# Install Python dependencies
poetry install

# Install Node dependencies for Tailwind
cd styling/static_src
npm install
cd ../..

# Build Tailwind CSS
poetry run python manage.py tailwind build

# Convert static asset files
poetry run python manage.py collectstatic --no-input

# Apply any outstanding database migrations
poetry run python manage.py migrate
