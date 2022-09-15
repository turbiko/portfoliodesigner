#!/bin/sh

python manage.py makemigrations --settings=core.settings.dev
python manage.py migrate --settings=core.settings.dev
#python manage.py update_index --settings=core.settings.dev
gunicorn core.wsgi:application -b :8000
exec "$@"