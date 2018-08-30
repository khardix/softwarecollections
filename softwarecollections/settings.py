"""
Django settings for softwarecollections project.

Generated by 'django-admin startproject' using Django 1.9.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os

import dj_database_url

# import ugettext_lazy to avoid circular module import
from django.utils.translation import ugettext_lazy as _  # noqa: F401

# Environment-dependent settings; defaults are suitable for development, unsuitable for production!

BASE_DIR = os.getenv(
    "SOFTWARECOLLECTIONS_BASE_DIR", default=os.path.dirname(os.path.dirname(__file__))
)

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv(
    "SOFTWARECOLLECTIONS_SECRET_KEY",
    default="m0zn_p7x*o(xvk^9p8_$6n7o)dn$bh-*_*xu*b!mg9$ihh0xu+",
)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = bool(os.getenv("DEBUG", default="True"))
DBDEBUG = os.getenv("DEBUG", default="") == "DB"

DATABASES = {
    "default": dj_database_url.config(
        env="SOFTWARECOLLECTIONS_DATABASE_URL",
        default="sqlite:///{path}".format(
            path=os.path.abspath(os.path.join(BASE_DIR, "data", "db.sqlite3"))
        ),
    )
}

# Application definition

ALLOWED_HOSTS = ["*"] if DEBUG else ["www.softwarecollections.org"]

# Emails
# https://docs.djangoproject.com/en/2.1/ref/settings/#std:setting-ADMINS
# https://docs.djangoproject.com/en/2.1/ref/settings/#std:setting-MANAGERS
# https://docs.djangoproject.com/en/2.1/ref/settings/#std:setting-SERVER_EMAIL
ADMINS = [
    ("Miroslav Suchý", "msuchy@redhat.com"),
    ("Adam Samalik", "asamalik@redhat.com"),
]
MANAGERS = ADMINS
SERVER_EMAIL = "SoftwareCollections @ {} <admin@softwarecollections.org>".format(
    os.uname().nodename
)

INSTALLED_APPS = [
    "softwarecollections",
    "softwarecollections.scls",
    "softwarecollections.auth",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_markdown2",
    "tagging",
    "sekizai",
    "captcha",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "softwarecollections.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "sekizai.context_processors.sekizai",
            ]
        },
    }
]

WSGI_APPLICATION = "softwarecollections.wsgi.application"

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {"level": "DEBUG", "class": "logging.StreamHandler"},
        "mail_admins": {
            "level": "ERROR",
            "class": "django.utils.log.AdminEmailHandler",
        },
    },
    "loggers": {
        "": {
            "handlers": DEBUG and ["console"] or ["console", "mail_admins"],
            "level": DEBUG and "DEBUG" or "INFO",
            "propagate": True,
        },
        "django.request": {
            "handlers": ["console", "mail_admins"],
            "level": "ERROR",
            "propagate": True,
        },
        "django.db.backends": {
            "level": DBDEBUG and "DEBUG" or "INFO",
            "propagate": True,
        },
    },
}


# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

USE_I18N = True

USE_L10N = True

USE_TZ = True

LANGUAGE_CODE = "en"

TIME_ZONE = "UTC"

LANGUAGES = (
    ("en", "English"),
    # ('cs', 'Čeština'),
)

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "htdocs", "media")

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = "/media/"

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "htdocs", "static")

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = "/static/"

# Absolute path to the directory repos should be synced to.
REPOS_ROOT = os.path.join(BASE_DIR, "htdocs", "repos")

# URL prefix for repo.
REPOS_URL = "/repos/"

# Absolute path to the directory used by yum cache
YUM_CACHE_ROOT = "/tmp/softwarecollections-yum-cache"

# Absolute path to the directory to be used as rpm _topdir
RPMBUILD_TOPDIR = "/tmp/softwarecollections-rpmbuild"

##################
# AUTHENTICATION #
##################

AUTH_USER_MODEL = "auth.User"

AUTHENTICATION_BACKENDS = (
    "softwarecollections.auth.backend.PerObjectModelBackend",
    "fas.backend.FasBackend",
)

LOGIN_URL = "/login/"

LOGOUT_URL = "/logout/"

LOGIN_REDIRECT_URL = LOGOUT_REDIRECT_URL = "/"

# The number of days a password reset link is valid for
PASSWORD_RESET_TIMEOUT_DAYS = 3

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.memcached.MemcachedCache",
        "LOCATION": os.getenv("MEMCACHE_LOCATION", default="127.0.0.1:11211"),
        "KEY_PREFIX": "softwarecollections",
    }
}

SESSION_ENGINE = "django.contrib.sessions.backends.cache"

CAPTCHA_FONT_SIZE = 32
CAPTCHA_LETTER_ROTATION = None
CAPTCHA_BACKGROUND_COLOR = "#ffffff"
CAPTCHA_FOREGROUND_COLOR = "#001100"
CAPTCHA_CHALLENGE_FUNCT = "captcha.helpers.math_challenge"
CAPTCHA_NOISE_FUNCTIONS = ()
CAPTCHA_FILTER_FUNCTIONS = ()
CAPTCHA_FLITE_PATH = "/usr/bin/flite"
CAPTCHA_TIMEOUT = 20

# COPR
COPR_URL = "https://copr.fedorainfracloud.org"
COPR_API_URL = COPR_URL + "/api"
COPR_COPRS_URL = COPR_URL + "/coprs"
