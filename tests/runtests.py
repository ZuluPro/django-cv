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
STATIC_ROOT = os.path.join(BASE_DIR, 'tests/static')
STATIC_URL = '/static/'
INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.admin',
    'django.contrib.staticfiles',
    'testapp',
    'curriculum',
    'curriculum.revealjs',
)
MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)
try:
    DEBUG_TOOLBAR_CONFIG = {}
    INTERNAL_IPS = ['192.168.254.2']
    __import__('imp').find_module('debug_toolbar')
    def show(request):
        True
    INSTALLED_APPS += ('debug_toolbar',)
    MIDDLEWARE_CLASSES = ('debug_toolbar.middleware.DebugToolbarMiddleware',)\
        + MIDDLEWARE_CLASSES
except ImportError:
    SHOW_TOOLBAR_CALLBACK = None

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.template.context_processors.media',
    'django.template.context_processors.static',
    'django.contrib.messages.context_processors.messages',
)
TEMPLATE_LOADERS = (
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
    STATIC_URL=STATIC_URL,
    STATIC_ROOT=STATIC_ROOT,
    # DEBUG_TOOLBAR_CONFIG=DEBUG_TOOLBAR_CONFIG
    INTERNAL_IPS=INTERNAL_IPS
)


def main():
    if django.VERSION >= (1, 7):
        django.setup()
    command_args = sys.argv[1:] or ['test', 'curriculum']
    call_command(*command_args)
    exit(0)

if __name__ == '__main__':
    main()
