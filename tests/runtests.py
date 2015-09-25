#!/usr/bin/env python
"""
Configuration and launcher for dbbackup tests.
"""
import os
import sys
import django
from django.conf import settings
from django.core.management import call_command

# Add testproject dbbackup in path
HERE = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.dirname(HERE)
sys.path[0:0] = [HERE, PARENT_DIR]

# Settings
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MEDIA_ROOT = os.path.join(BASE_DIR, 'tests/media')
MEDIA_URL = '/media/'
INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.admin',
    'django.contrib.staticfiles',
    'testapp',
    'curriculum',
)
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.template.context_processors.media',
    'django.template.context_processors.static',
    'django.contrib.messages.context_processors.messages',
)
TEMPLATE_LOADERS = (
)
MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': TEMPLATE_CONTEXT_PROCESSORS
        }
    },
]


settings.configure(
    DEBUG=True,
    ADMIN=('foo@bar'),
    ALLOWED_HOSTS=['*'],
    MEDIA_ROOT=MEDIA_ROOT,
    MEDIA_URL=MEDIA_URL,
    MIDDLEWARE_CLASSES=MIDDLEWARE_CLASSES,
    # CACHES={'default': {'BACKEND': 'django.core.cache.backends.locmem.LocMemCache'}},
    INSTALLED_APPS=INSTALLED_APPS,
    DATABASES={'default': {'ENGINE': 'django.db.backends.sqlite3', 'NAME': 'db.sqlite'}},
    ROOT_URLCONF='urls',
    SECRET_KEY="it's a secret to everyone",
    SITE_ID=1,
    TEMPLATES=TEMPLATES,
    BASE_DIR=BASE_DIR,
    STATIC_URL='/static/',
)


def main():
    if django.VERSION >= (1, 7):
        django.setup()
    command_args = sys.argv[1:] or ['test', 'curriculum']
    call_command(*command_args)
    exit(0)

if __name__ == '__main__':
    main()
