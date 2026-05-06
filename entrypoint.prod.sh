#!/bin/bash
set -e

echo "Running migrations..."
python manage.py migrate --noinput

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Creating superuser if needed..."
python manage.py shell <<EOF
from django.contrib.auth.models import User
if not User.objects.filter(username='admin').exists():
    u = User.objects.create_superuser('admin', '', '$ADMIN_PASSWORD')
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
