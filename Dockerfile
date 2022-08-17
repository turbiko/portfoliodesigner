FROM python:3.10.4-slim-buster
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
COPY . /app

CMD set -xe; python manage.py migrate --noinput; python manage.py runserver 0.0.0.0:8000