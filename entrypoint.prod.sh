#!/bin/bash
export DJANGO_SETTINGS_MODULE=test_project.settings_prod
set -e

echo "Running migrations..."
python manage.py migrate --noinput

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Creating superuser if needed..."
python manage.py shell <<EOF
from django.contrib.auth.models import User
import os
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', '', os.environ.get('ADMIN_PASSWORD', 'admin123'))
    print("Superuser created.")
else:
    print("Superuser already exists.")
EOF

echo "Starting gunicorn..."
exec gunicorn test_project.wsgi:application \
    --bind 0.0.0.0:8000 \
    --workers ${GUNICORN_WORKERS:-2} \
    --timeout 120 \
    --access-logfile -
