#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -o errexit

# Install dependencies (Render already does this in build, so this is optional)
# pip install -r requirements.txt

# Run database migrations
python manage.py migrate --noinput

# Collect static files
python manage.py collectstatic --noinput

# Optional: create superuser (only runs if user doesn’t exist)
# echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.filter(username='admin').exists() or User.objects.create_superuser('admin', 'admin@example.com', 'adminpass')" | python manage.py shell

# Start Gunicorn server
gunicorn portfolio.wsgi:application --bind 0.0.0.0:$PORT
