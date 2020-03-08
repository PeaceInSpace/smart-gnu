"""
Django settings for smartGNU project.

Generated by 'django-admin startproject' using Django 3.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'd%4ok*5ionsw*sxbk^mpve^e^z0j%ccv9ya3vfe0)2f#*ye8tq'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']
CORS_ORIGIN_ALLOW_ALL=True

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework.authtoken',
    'rest_framework',
    'rest_framework_swagger',
    'constance',
    'smart_gnu',
    'corsheaders'
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'smartGNU.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'smartGNU.wsgi.application'


# CHANNEL_LAYERS = {
#     'default': {
#         'BACKEND': 'channels_redis.core.RedisChannelLayer',
#         'CONFIG': {
#             "hosts": [CHANNEL_REDIS_HOST],
#             "symmetric_encryption_keys": [SECRET_KEY],
#         },
#     },
# }
# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'smartgnudb',
        'USER': 'smartgnuuser',
        'PASSWORD': 'smartgnu8198',
        'HOST': '104.198.97.15',
        'PORT': '5432',
    }
}

REST_FRAMEWORK = {

    # Use Django's standard `django.contrib.auth` permissions,

    # or allow read-only access for unauthenticated users.

    'DEFAULT_AUTHENTICATION_CLASSES': (

          'rest_framework.authentication.TokenAuthentication',
    ),

    'DEFAULT_PERMISSION_CLASSES': (

        'rest_framework.permissions.IsAuthenticated',

        # 'rest_framework.permissions.AllowAny',

    ),

    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend']

}

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, 'static')



STATIC_URL = '/static/'
# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'smart_gnu/static'),
)


SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {
        'api_key': {
            'type': 'apiKey',
            'in': 'header',
            'name': 'Authorization'
        }
    },
}

CONSTANCE_BACKEND = 'constance.backends.database.DatabaseBackend'
CONSTANCE_IGNORE_ADMIN_VERSION_CHECK = True
CONSTANCE_CONFIG = {
    'MQTT_USERNAME': ('ngtyutmq', 'mqtt username',str),
    'MQTT_PASSWORD': ('mItz0RMt1UtC', 'mqtt password',str),
    'MQTT_SERVER': ('hairdresser.cloudmqtt.com', 'mqtt server address',str),
    'MQTT_PUBLIC_PORT': (16642, 'mqtt public port',int),
    'MQTT_SECURE_PORT': (0, 'mqtt ssl port',int),
    'GOOGLE_CLIENT_ID' : ("85906610984-qog0si0va6si6tnj3tij46b7r3gv9n8g.apps.googleusercontent.com",
                          'goole console client id',str),
}

CONSTANCE_CONFIG_FIELDSETS = {
    'MQTT Options': ('MQTT_USERNAME', 'MQTT_PASSWORD','MQTT_SERVER','MQTT_PUBLIC_PORT','MQTT_SECURE_PORT'),
    'Google options': ('GOOGLE_CLIENT_ID',)
}

try:
    from .local_settings import *
except ImportError:
    pass