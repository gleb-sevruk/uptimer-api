import logging

from django.conf import settings

git_commit_hash = settings.GIT_COMMIT_HASH
logging_env = settings.LOGGING_ENVIRONMENT
app = settings.LOGGING_APP
custom_tags = settings.LOGGING_CUSTOM_TAGS

class ExtendedFieldsFilter(logging.Filter):
    environment = None
    def __init__(self):
        super().__init__()

    def filter(self, record):
        emit = True
        record.git_commit_hash = git_commit_hash
        record.environment = logging_env
        record.application_name = app
        record.custom_tags = custom_tags

        return emit