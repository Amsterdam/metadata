#!/usr/bin/env bash

set -u
set -e

cd /app

# migrate database tables
yes yes | python manage.py migrate --noinput

echo Collecting static files
yes yes | python manage.py collectstatic

ls -al /static/

chmod -R 777 /static

# run uwsgi
exec uwsgi
