import os
DIRNAME = os.path.dirname(__file__)

DEFAULT_CHARSET = 'utf-8'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'tagging_test',
    },
}


INSTALLED_APPS = (
    'django.contrib.contenttypes',
    'tagging',
    'tagging.tests',
)
