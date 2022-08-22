FROM python:3.9.5-slim-buster
ENV PYTHONUNBUFFERED 1
RUN pip install "gunicorn==20.0.4"
# Install system packages required by Wagtail and Django.
RUN apt-get update --yes --quiet && apt-get install --yes --quiet --no-install-recommends \
    build-essential \
    libpq-dev \
    libmariadbclient-dev \
    libjpeg62-turbo-dev \
    zlib1g-dev \
    libwebp-dev \
 && rm -rf /var/lib/apt/lists/*
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
COPY . /app
# RUN python manage.py collectstatic
# CMD set -xe; python manage.py migrate --noinput; python manage.py runserver 0.0.0.0:8000
CMD set -xe; python manage.py migrate --noinput; gunicorn core.wsgi:application -b :8000