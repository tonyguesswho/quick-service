#!/bin/sh

echo "Waiting for postgres..."

while ! nc -z api-db 5432; do
  sleep 0.1
done

echo "PostgreSQL started"

python -m pytest "src/tests"
python manage.py recreate_db
# python manage.py seed_db
# flake8 src
# black src --check
# isort src --check-only
python manage.py run -h 0.0.0.0