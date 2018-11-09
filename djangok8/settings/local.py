import dj_database_url

from .common import *

# postgres://USER:PASSWORD@HOST:PORT/NAME
DATABASES = {
    'default': dj_database_url.config(
      default='postgres://postgres:postgres@172.20.0.3/postgres'
    ),
}


LOGGING_ENVIRONMENT = 'local'

ROOT_LOGGER_PROJECT_NAME = 'djangok8'

