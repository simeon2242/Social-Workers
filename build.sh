#!/usr/bin/env bash

set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input

python manage.py migrate

if [ "$CREATE_SUPERUSER" = "true" ]; then
    python manage.py ensure_admin \
        --username "$DJANGO_SUPERUSER_USERNAME" \
        --password "$DJANGO_SUPERUSER_PASSWORD" \
        --email "$DJANGO_SUPERUSER_EMAIL"
fi

if [ "$SEED_DEMO" = "true" ]; then
    python manage.py seed_demo
fi