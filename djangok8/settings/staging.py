import dj_database_url

from .common import *

# postgres://USER:PASSWORD@HOST:PORT/NAME
# DATABASES = {
#     'default': dj_database_url.config(
#       default='postgres://postgres:postgres@172.20.0.3/postgres'
#     ),
# }

LOGGING_ENVIRONMENT = 'staging'
# postgres://USER:PASSWORD@HOST:PORT/NAME
DATABASES = {
    'default': dj_database_url.config(
      env='ENV_DATABASE_URL',
      default='postgres://postgres:5HE1Br0eRb@db-postgresql.gitlab-4.svc.cluster.local/postgres'
    ),
}
