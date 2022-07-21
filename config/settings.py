import logging.config
import os
from datetime import timedelta

import dj_database_url
from django.core.exceptions import ImproperlyConfigured

project_root = os.path.dirname(__file__)


def get_env_var(var_name):
    try:
        env_var = os.environ[var_name]
        if "True" == env_var:
            return True
        elif "False" == env_var:
            return False
        else:
            return env_var
    except KeyError:
        raise ImproperlyConfigured(f"Set the {var_name} environment variable")


# ENVIRONMENT
# ------------------------------------------------------------------------------

ENVIRONMENT = get_env_var("ENVIRONMENT")

# STATIC DIRS
# ------------------------------------------------------------------------------

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
CONTENT_DIR = os.path.join(BASE_DIR, "static")


# SECRET KEY
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/1.10/ref/settings/#std:setting-SECRET_KEY
# SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY = os.getenv("SECRET_KEY")

# DEBUG
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/1.10/ref/settings/#debug
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = get_env_var("DEBUG")


# MANAGER CONFIGURATION
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/1.10/ref/settings/#admins
# https://docs.djangoproject.com/en/1.10/ref/settings/#managers

ADMINS = (("""Adam Aaron Mischke""", "mischke@protonmail.com"),)

MANAGERS = ADMINS

ALLOWED_HOSTS = ["*"]

https_only = os.getenv("SECURE_SSL_REDIRECT", True)
SECURE_SSL_REDIRECT = https_only == "True"

# APP CONFIGURATION
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/1.10/ref/settings/#installed-apps

DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.db.migrations.migration",
    "django.contrib.staticfiles",
    "corsheaders",
    "django_extensions",
    "django.forms",
]

THIRD_PARTY_APPS = [
    "whitenoise.runserver_nostatic",
    "rest_framework_simplejwt.token_blacklist",
    "solo",
    "silk",
]

LOCAL_APPS = ["config", "users"]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

# MIDDLEWARE CONFIGURATION
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/1.10/topics/http/middleware/

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "silk.middleware.SilkyMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
]

# CORS Configuration
CORS_ALLOW_ALL_ORIGINS = os.getenv("CORS_ALLOW_ALL_ORIGINS") == "True"
if os.getenv("CORS_ALLOWED_ORIGINS"):
    CORS_ALLOWED_ORIGINS = os.getenv("CORS_ALLOWED_ORIGINS").split(" ")
if os.getenv("CSRF_TRUSTED_ORIGINS"):
    CSRF_TRUSTED_ORIGINS = os.getenv("CSRF_TRUSTED_ORIGINS").split(" ")
CORS_ALLOW_HEADERS = (
    "content-disposition",
    "accept-encoding",
    "content-type",
    "accept",
    "origin",
    "authorization",
    "signature",
)


# URL Configuration
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/1.10/ref/settings/#root-urlconf

ROOT_URLCONF = "config.urls"


# TEMPLATE CONFIGURATION
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/1.10/topics/templates/


FORM_RENDERER = "django.forms.renderers.TemplatesSetting"
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(CONTENT_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ]
        },
    }
]

# WGSI CONFIGURATION
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/1.10/ref/settings/#wsgi-application

WSGI_APPLICATION = "config.wsgi.application"

# DATABASE CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    "default": dj_database_url.config(
        default="postgres://postgres_user:postgres_password@postgres:5432/postgres_db"
    )
}

# PASSWORD VALIDATION
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation."
        "UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# AUTHENTICATION
# ------------------------------------------------------------------------------

AUTHENTICATION_BACKENDS = ["django.contrib.auth.backends.ModelBackend"]

# GENERAL CONFIGURATION
# ------------------------------------------------------------------------------
# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
# https://docs.djangoproject.com/en/1.10/topics/i18n/


LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True

SITE_ID = 1


# STATIC FILE CONFIGURATION
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_ROOT = os.path.join(CONTENT_DIR, "static")
STATIC_URL = "/static/"

MEDIA_ROOT = os.path.join(CONTENT_DIR, "media")
MEDIA_URL = "/media/"

STATICFILES_DIRS = [os.path.join(CONTENT_DIR, "assets")]


# Logging Configuration
# ------------------------------------------------------------------------------
#

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "root": {"format": "%(levelname)-8s %(message)s"},
        "console": {"format": "%(name)-12s %(levelname)-8s %(message)s"},
        "worker": {"format": "%(name)-50s %(levelname)-8s | %(message)s"},
    },
    "handlers": {
        "root": {"class": "logging.StreamHandler", "formatter": "root"},
        "console": {"class": "logging.StreamHandler", "formatter": "console"},
        "worker": {"class": "logging.StreamHandler", "formatter": "worker"},
    },
    "loggers": {
        "": {"handlers": ["root"], "level": os.getenv("LOG_LEVEL", "warning").upper()},
        "django.db.backends": {"level": os.getenv("DATABASE_LOG_LEVEL", "INFO")},
        "django.request": {"level": os.getenv("LOG_LEVEL", "DEBUG").upper()},
    },
}
logging.config.dictConfig(LOGGING)


AUTH_USER_MODEL = "users.User"

# Silky
# ------------------------------------------------------------------------------
#
SILKY_INTERCEPT_PERCENT = int(get_env_var("SILKY_INTERCEPT_PERCENT"))
SILKY_PYTHON_PROFILER = True
SILKY_AUTHENTICATION = True  # User must login
SILKY_AUTHORISATION = True  # User must have permissions
# SILKY_PERMISSIONS = lambda user: user.is_superuser
SILKY_META = True  # see what effect Silk is having on the request/response time
SILKY_ANALYZE_QUERIES = True

# SIMPLE JWT
# ------------------------------------------------------------------------------
#
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(days=7),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=365),
    "ROTATE_REFRESH_TOKENS": False,
    "BLACKLIST_AFTER_ROTATION": False,
    "UPDATE_LAST_LOGIN": False,
    "ALGORITHM": "HS256",
    "SIGNING_KEY": SECRET_KEY,
    "VERIFYING_KEY": None,
    "AUDIENCE": None,
    "ISSUER": None,
    "JWK_URL": None,
    "LEEWAY": 0,
    "AUTH_HEADER_TYPES": ("Bearer",),
    "AUTH_HEADER_NAME": "HTTP_AUTHORIZATION",
    "USER_ID_FIELD": "id",
    "USER_ID_CLAIM": "user_id",
    "USER_AUTHENTICATION_RULE": (
        "rest_framework_simplejwt.authentication.default_user_authentication_rule"
    ),
    "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
    "TOKEN_TYPE_CLAIM": "token_type",
    "TOKEN_USER_CLASS": "rest_framework_simplejwt.models.TokenUser",
    "JTI_CLAIM": "jti",
}


# Prints
# ------------------------------------------------------------------------------
#

print("ENVIRONMENT is", ENVIRONMENT)
print("CORS_ALLOW_ALL_ORIGINS is", CORS_ALLOW_ALL_ORIGINS)
if os.getenv("CORS_ALLOWED_ORIGINS"):
    print("CORS_ALLOWED_ORIGINS is", CORS_ALLOWED_ORIGINS)
if os.getenv("CSRF_TRUSTED_ORIGINS"):
    print("CSRF_TRUSTED_ORIGINS is", CSRF_TRUSTED_ORIGINS)
print("DEBUG is", DEBUG)
print("SSL is", SECURE_SSL_REDIRECT)
