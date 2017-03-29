#!/usr/bin/env bash

set -u
set -e

cd /app

source docker-wait.sh

# migrate database tables
yes yes | python manage.py migrate --noinput

# run uwsgi
exec uwsgi
