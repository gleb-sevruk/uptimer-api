FROM python:3.6

MAINTAINER GS

ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y \
  cron \
  rsyslog \
  supervisor \
  &&  pip install circus \
  &&  pip install gunicorn

RUN touch /var/log/cron.log
RUN chmod 0666 /var/log/cron.log

RUN mkdir /code
RUN mkdir /my_django_data

WORKDIR /code


ADD requirements.txt /code/

ARG BA_REQUIREMENTS_FILE=requirements.txt
ENV BA_REQUIREMENTS_FILE ${BA_REQUIREMENTS_FILE}

RUN pip install -r ${BA_REQUIREMENTS_FILE}

COPY . /code

ENV DJANGO_SETTINGS_MODULE djangok8.settings.production



CMD (/code/deployment/run_web.sh)