# --- Tailwind CSS build ---
FROM node:20-slim AS css
WORKDIR /src
COPY . .
RUN cd styling/static_src && npm ci && npm run build

# --- App ---
FROM python:3.12-slim-bookworm
RUN useradd --create-home app
ENV PYTHONUNBUFFERED=1 PORT=8000 POETRY_VIRTUALENVS_CREATE=false
RUN apt-get update && apt-get install -y --no-install-recommends \
      build-essential libjpeg62-turbo-dev zlib1g-dev libwebp-dev \
    && rm -rf /var/lib/apt/lists/*
WORKDIR /app
COPY pyproject.toml poetry.lock ./
RUN pip install --no-cache-dir poetry && poetry install --only main --no-root
COPY . .
COPY --from=css /src/styling/static/css/dist ./styling/static/css/dist
RUN mkdir -p /app/data /app/backups && chown -R app:app /app
USER app
RUN DJANGO_SETTINGS_MODULE=jrbenriquez.settings.production SECRET_KEY=build-only \
    DJANGO_ALLOWED_HOSTS=localhost python manage.py collectstatic --noinput
EXPOSE 8000
CMD set -xe; python manage.py migrate --noinput; exec gunicorn jrbenriquez.wsgi:application --bind 0.0.0.0:${PORT} --workers ${WEB_CONCURRENCY:-2}
