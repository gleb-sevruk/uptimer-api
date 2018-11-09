#!/usr/bin/env bash

export BA_REQUIREMENTS_FILE=requirements.txt
export DJANGO_SETTINGS_MODULE=djangok8.settings.staging

# postgres://USER:PASSWORD@HOST:PORT/NAME
export ENV_DATABASE_URL=postgres://postgres:postgres@db/dev_django


export DOMAIN=dev.django.dealer-advance.com
export ENABLE_REDIRECT=true
export LOGGING_CUSTOM_TAGS="dev;dev.django;inside-docker;"

