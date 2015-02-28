# -*- coding: UTF-8 -*-
# settings/local.py
#import os
from my_blog.settings.common import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = []

#EMAIL_BACKEND = 'django.core.email.backends.console.EmailBackend'

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db1.sqlite3'),
    }
}

#INSTALLED_APPS += ("debug_toolbar",)
