#!/usr/bin/env bash

set -u
set -e

cd /app

# migrate database tables
yes yes | python manage.py migrate --noinput

# run uwsgi
exec uwsgi --ini /app/uwsgi.ini
