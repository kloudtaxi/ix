"""
Django settings for ix.server project.

Generated by 'django-admin startproject' using Django 4.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""
import logging
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ["DJANGO_SECRET_KEY"]

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

DOCKER_HOST_IP = "172.17.42.1"

ALLOWED_HOSTS = [
    "localhost",
    "0.0.0.0",
    "127.0.0.1",
]


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "graphene_django",
    "channels",
    "django_extensions",
    "ix.ix_users",
    "ix.task_log",
    "ix.chains",
    "ix.agents",
    "ix.chat",
    "ix.datasources",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "ix.server.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": ["/var/app/ix/templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "ix.server.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "ix",
        "USER": "ix",
        "PASSWORD": "ix",
        "HOST": "db",
        "PORT": "5432",
    }
}


AUTH_USER_MODEL = "ix_users.User"

# filter objects by ownership, disable for local deployments
OWNER_FILTERING = os.environ.get("OWNER_FILTERING", "0") == "1"

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = "static/"

STATICFILES_DIRS = [
    # BASE_DIR / "static",
    "/var/app/frontend/static/",
    "/var/app/.compiled-static/",
]

# STATICFILES_FINDERS


# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

GRAPHENE = {"SCHEMA": "ix.schema.schema"}

ASGI_APPLICATION = "ix.server.asgi.application"

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [("redis", 6379)],
        },
    },
}

# Celery configuration
CELERY_BROKER_URL = "redis://redis:6379/2"
CELERY_RESULT_BACKEND = "redis://redis:6379/2"

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://redis:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        },
    }
}


SHELL_PLUS_PRE_IMPORTS = (("ix.task_log.models", "*"), ("ix.task_log.tests.fake", "*"))


LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {"class": "logging.StreamHandler", "formatter": "colorful"}
    },
    "formatters": {
        "colorful": {
            "()": "colorlog.ColoredFormatter",
            "format": "%(asctime)s %(log_color)s%(levelname)s%(reset)s %(message)s ",
            "datefmt": "%Y-%m-%d %H:%M:%S",
            "log_colors": {
                "DEBUG": "cyan",
                "INFO": "white",
                "WARNING": "yellow",
                "ERROR": "red",
                "CRITICAL": "red,bg_white",
            },
        }
    },
    "loggers": {
        "ix": {
            "handlers": ["console"],
            "level": logging.DEBUG,
        },
    },
}

MOCK_CHAT_RESPONSE = os.environ.get("MOCK_CHAT_RESPONSE", False)

# Default agents to include in chats
DEFAULT_AGENTS = [
    "b7d8f662-12f6-4525-b07b-c9ea7c10010a",  # @code
    "cc054ff5-67cd-4489-b0f1-b8b62af2d825",  # @readme
]


# Dev environment can load from .vault.env
# TODO: move this to dev_settings if possible.
if os.path.exists("/var/app/.vault.env"):
    with open("/var/app/.vault.env", "r") as f:
        key_file = f.read()
        key, value = key_file.strip().split("=")
        os.environ["VAULT_ROOT_KEY"] = value

VAULT_ROOT_KEY = "myroot"
VAULT_SERVER = os.environ.get("VAULT_SERVER", "https://vault:8200")
VAULT_TOKEN__USER_TOKENS = VAULT_ROOT_KEY
VAULT_CLIENT_CRT = "/var/vault/certs/client.crt"
VAULT_CLIENT_KEY = "/var/vault/certs/client.key"
VAULT_TLS_VERIFY = False
