"""
Django settings for djangoTrade project.

Generated by 'django-admin startproject' using Django 1.11.1.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""
from __future__ import absolute_import, unicode_literals
import os

# Celery options
from kombu import Queue, Exchange

CELERY_BROKER_URL = 'amqp://guest:guest@localhost//'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_RESULT_BACKEND = 'db+mysql://root:@localhost/celery_result'
CELERY_TASK_SERIALIZER = 'json'
CELERY_TIMEZONE = 'Europe/Moscow'
CELERY_SEND_TASK_ERROR_EMAILS = False
CELERYD_MAX_TASKS_PER_CHILD = 5

CELERY_ROUTES = {
    'trade.tasks.pull_exchanges_balances': {'queue': 'low'},
    'trade.tasks.pull_exchanges_tickers': {'queue': 'low'},
}

CELERY_CREATE_MISSING_QUEUES = True

# AllAuth setting
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_AUTHENTICATION_METHOD = 'username_email'
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 1
LOGIN_REDIRECT_URL = '/'
ACCOUNT_LOGOUT_REDIRECT_URL = '/'
ACCOUNT_LOGOUT_ON_PASSWORD_CHANGE = True

# redis sessions
SESSION_ENGINE = 'redis_sessions.session'

# Email
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

DEFAULT_INDEX_TABLESPACE = 10

ADMINS = (('Сергей', 'achievement008@gmail.com'),)

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '1j&=q!62_%51y9!=97n=)bel8+#y+lup1bsy31d%s=sm!9q_c+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'trade',
    'tradeBOT',
    'user_profile',
    'django_celery_beat',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'django.contrib.humanize',
    'ticker_app',
    'django_extensions',
    'channels',
]

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

ROOT_URLCONF = 'djangoTrade.urls'

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

WSGI_APPLICATION = 'djangoTrade.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'trade',
        'USER': 'root',
        'PASSWORD': '',
        'default-character-set': 'utf-8',
    },
    'portal_ticker': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'portal_ticker',
        'USER': 'root',
        'PASSWORD': '',
    }
}

DATABASE_ROUTERS = ['ticker_app.routers.DBRouter', 'ticker_app.routers.PrimaryRouter']

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-US'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'

LOGIN_URL = '/accounts/login/'

# yandex money settings
YANDEX_MONEY_CLIENT_ID = None  # set before start

YANDEX_MONEY_REDIRECT_URI = None  # set before start

YANDEX_MONEY_CLIENT_SECRET = None  # set before start

STATIC_ROOT = '/opt/portal_ongrid/static'
MEDIA_ROOT = '/opt/portal_ongrid/media'
MEDIA_URL = '/media/'

# channels
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "asgi_redis.RedisChannelLayer",
        "CONFIG": {
            "hosts": [("localhost", 6379)],
        },
        "ROUTING": "djangoTrade.routing.channel_routing",
    },
}

# минимальное значение изменения цены за секунду
DEPTH_COEFFICIENT = 0.5

# активные биржи для торговли
TRADING_EXCHANGES = ['poloniex']

# Time to life order, mins
ORDER_TTL = 5

# минимальное кол-во элементов серии
RATE_CHANGE_SERIES_MIN_COUNT = 2

# количество направлений
DIRECTIONS_COUNT = 7

# количество однонапрвленных (первых) направлений
UNIDIRECTIONAL_COUNT = 4
