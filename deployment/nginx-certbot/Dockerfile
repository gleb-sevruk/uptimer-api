FROM python:3.6

MAINTAINER Intuitive Web Solutions

ENV PYTHONUNBUFFERED 1

RUN apt-get update && \
        apt-get install -y --no-install-recommends \
        nginx \
        cron

RUN pip install letsencrypt certbot
RUN mkdir -p /cert_folder
RUN mkdir -p /my_django_data/.well-known
CMD (/cert_folder/run.sh)
