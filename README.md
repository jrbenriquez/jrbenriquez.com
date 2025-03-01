# Personal Blog

This project is based on the official Wagtail documentation for a portfolio/blog site, but uses **Poetry** instead of a traditional virtual environment.

## Quick Setup Guide

### 1. Clone the Repository
```sh
git clone <your-repo-url>
cd <your-project-folder>
```

### 2. Install Dependencies
Ensure **Poetry** is installed. If not, install it first:
```sh
curl -sSL https://install.python-poetry.org | python3 -
```
Then install project dependencies:
```sh
poetry install
```

### 3. Apply Migrations
```sh
poetry run python manage.py migrate
```

### 4. Create a Superuser
```sh
poetry run python manage.py createsuperuser
```

### 5. Run the Development Server
```sh
poetry run python manage.py runserver
```
Now, visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser.

## Additional Commands

### Collect Static Files
```sh
poetry run python manage.py collectstatic
```

### Load Sample Data (if available)
```sh
poetry run python manage.py loaddata <fixture-file>
```
