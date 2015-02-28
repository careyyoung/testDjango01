# -*- coding: UTF-8 -*-
"""
Django settings for my_blog project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!


# Application definition

INSTALLED_APPS = (
    #'django_admin_bootstrapped.bootstrap3',
    #'django_admin_bootstrapped',
    'bootstrap_admin',  # 一定要放在`django.contrib.admin`前面
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'article',
    'test01',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)


from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS
TEMPLATE_CONTEXT_PROCESSORS = TEMPLATE_CONTEXT_PROCESSORS + (
    'django.core.context_processors.request',
)
#print TEMPLATE_CONTEXT_PROCESSORS
BOOTSTRAP_ADMIN_SIDEBAR_MENU = True



ROOT_URLCONF = 'my_blog.urls'

WSGI_APPLICATION = 'my_blog.wsgi.application'

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'g9hd0y%!f00*l-lx7o+^stna!ogf$&6ell#vcc29xa(u9eql6k'

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'zh-cn'

TIME_ZONE = 'asia/shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/


STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    ("js", os.path.join(STATIC_ROOT, 'js')),
    ("css", os.path.join(STATIC_ROOT, 'css')),
    ("img", os.path.join(STATIC_ROOT, 'img')),
    
    # os.path.join(BASE_DIR, "static").replace('\\', '/'), #把静态文件放project下的 static文件夹
    # '/var/www/static/', #静态文件放在  /var/www/static/中
    )


MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
MEDIA_DIRS = (
    os.path.join(BASE_DIR, "media").replace('\\', '/'),  # 把media文件放project下的 media 文件夹
    )

TEMPLATE_DIRS = (
    #os.path.join(BASE_DIR, 'templates').replace('\\', '/'),  # 把模板文件放project下的 templates文件夹
    #os.path.join(BASE_DIR, 'test01/templates').replace('\\', '/'),  # app:test01下的templates文件夹
    )
