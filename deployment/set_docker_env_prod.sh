#!/usr/bin/env bash

export BA_REQUIREMENTS_FILE=requirements.txt
export DJANGO_SETTINGS_MODULE=djangok8.settings.production

export ENV_DATABASE_URL=postgres://postgres:postgres@db/prod_django

export BA_SENTRY_DSN=https://81b3788abd3d4785926568cbfe0eb32f:5ca35686459b4f4591a0342fa870eb04@sentry.io/287677
export DOMAIN=prod.django.dealer-advance.com
export ENABLE_REDIRECT=false
export LOGGING_CUSTOM_TAGS="prod;prod.django;inside-docker;"
