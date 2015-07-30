# -*- coding: utf-8 -*-
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'facebookapp',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '',
    }
}

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'config/static'),
)

MEDIA_URL = '/media/'
STATIC_URL = '/static/'
