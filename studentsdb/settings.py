"""
Django settings for studentsdb project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""
from django.conf import global_settings

import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

TEMPLATE_CONTEXT_PROCESSORS = global_settings.TEMPLATE_CONTEXT_PROCESSORS + ("django.core.context_processors.request",
"studentsdb.context_processors.students_proc",)

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '+nw4!0+b=w)d1atkjpt$n%=n(0f$s#h2k(d2v31qqyv#g+s2s1'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'crispy_forms',
    'students'
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

ROOT_URLCONF = 'studentsdb.urls'

WSGI_APPLICATION = 'studentsdb.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, '..', 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'uk'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

PORTAL_URL = 'http://localhost:8000'

# email settings
ADMIN_EMAIL = 'admin@studentsdb.com'
EMAIL_HOST = 'smtp.mandrillapp.com'
EMAIL_PORT = '587'
EMAIL_HOST_USER = 'taliana.slava@gmail.com'
EMAIL_HOST_PASSWORD = 'Efs35i7Tp.xfrQ4'
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, '..', 'media')

CRISPY_TEMPLATE_PACK = 'bootstrap3'
