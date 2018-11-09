import dj_database_url

from .common import *

# postgres://USER:PASSWORD@HOST:PORT/NAME
# DATABASES = {
#     'default': dj_database_url.config(
#       default='postgres://postgres:postgres@172.20.0.3/postgres'
#     ),
# }

LOGGING_ENVIRONMENT = 'production'

# postgres://USER:PASSWORD@HOST:PORT/NAME
DATABASES = {
    'default': dj_database_url.config(
      env='ENV_DATABASE_URL',
      default='postgres://postgres:72jH9qVPA7@django-postgresql.gitlab-djk8/postgres'
    ),
}

