#!/bin/sh

python manage.py makemigrations --settings=biz.settings.dev
python manage.py migrate --settings=biz.settings.dev
#python manage.py update_index --settings=biz.settings.dev
gunicorn biz.wsgi:application -b :8000
exec "$@"