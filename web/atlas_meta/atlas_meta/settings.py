# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import sys
from pathlib import Path


from datapunt_generic.generic.database import get_docker_host
from atlas_meta.settings_databases import (
    LocationKey,
    get_docker_host,
    get_database_key,
    OVERRIDE_HOST_ENV_VAR,
    OVERRIDE_PORT_ENV_VAR,
)


BASE_DIR = Path(__file__).resolve().parent.parent

insecure_secret = "default-secret"
SECRET_KEY = os.getenv("SECRET_KEY", insecure_secret)

DEBUG = SECRET_KEY == insecure_secret

TESTING = sys.argv[1:2] == ["test"]

ALLOWED_HOSTS = ["*"]

# Application definition

INSTALLED_APPS = (
    "django.contrib.admin",
    "django.contrib.contenttypes",
    "django.contrib.auth",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_extensions",
    "corsheaders",
    "rest_framework",
    "atlas",
)

if DEBUG:
    INSTALLED_APPS += ("debug_toolbar",)

MIDDLEWARE = (
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",
)

ROOT_URLCONF = "atlas_meta.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "atlas/templates")],
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

WSGI_APPLICATION = "atlas_meta.wsgi.application"

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASE_OPTIONS = {
    LocationKey.docker: {
        "ENGINE": "django.contrib.gis.db.backends.postgis",
        "NAME": os.getenv("DATABASE_NAME", "metadata"),
        "USER": os.getenv("DATABASE_USER", "metadata"),
        "PASSWORD": os.getenv("DATABASE_PASSWORD", "insecure"),
        "HOST": "database",
        "PORT": "5432",
    },
    LocationKey.local: {
        "ENGINE": "django.contrib.gis.db.backends.postgis",
        "NAME": os.getenv("DATABASE_NAME", "metadata"),
        "USER": os.getenv("DATABASE_USER", "metadata"),
        "PASSWORD": os.getenv("DATABASE_PASSWORD", "insecure"),
        "HOST": get_docker_host(),
        "PORT": "5405",
    },
    LocationKey.override: {
        "ENGINE": "django.contrib.gis.db.backends.postgis",
        "NAME": os.getenv("DATABASE_NAME", "metadata"),
        "USER": os.getenv("DATABASE_USER", "metadata"),
        "PASSWORD": os.getenv("DATABASE_PASSWORD", "insecure"),
        "HOST": os.getenv(OVERRIDE_HOST_ENV_VAR),
        "PORT": os.getenv(OVERRIDE_PORT_ENV_VAR, "5432"),
    },
}

DATABASES = {"default": DATABASE_OPTIONS[get_database_key()]}

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True


USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "static"
STORAGES = {
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}


HANDLERS = {
    "console": {
        "class": "logging.StreamHandler",
    }
}

# Only slack when running in 'prod' mode
if not DEBUG:
    HANDLERS.update(
        {
            "slack_handler": {
                "level": "ERROR",
                "class": "pyslack.SlackHandler",
                "formatter": "slack_formatter",
                "token": os.getenv("SLACK_TOKEN", "insecure"),
                "username": "atlas metadata",
                "channel": "#devops",
            }
        }
    )

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "slack_formatter": {
            "format": "%(message)s",
        },
    },
    "loggers": {
        "django": {
            "handlers": ["console"] if DEBUG else ["console", "slack_handler"],
            "level": "INFO",
        }
    },
}

LOGGING.update({"handlers": HANDLERS})

LOGIN_REDIRECT_URL = "/"
LOGIN_URL = "/login"

INTERNAL_IPS = ["127.0.0.1"]

# Security

SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
# CSRF_COOKIE_SECURE = True
CSRF_COOKIE_HTTPONLY = True
X_FRAME_OPTIONS = "DENY"

HEALTH_MODEL = "atlas.metadata"

CORS_ORIGIN_REGEX_WHITELIST = (
    "^(https?://)?localhost(:\d+)?$",
    "^(https?://)?.*\.data.amsterdam\.nl$",
    "^(https?://)?.*\.amsterdam\.nl$",
)
