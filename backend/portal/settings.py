# -*- coding: utf-8 -*-
import os

from pathlib import Path
# from django.utils.translation import gettext_lazy as _
# from django.utils.translation import gettext
from django.contrib.messages import constants as messages

# ********** Import configs: **********
# redis settings
from .config.redis import *

# logging settings
from .config.logging import *

# jupyter settings
# from .jupyter_settings import *

 

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get("DJANGO_DEVELOPMENT_SECRET_KEY", "admin")

DEBUG = int(os.environ.get("DEBUG", default=False))

# 'DJANGO_ALLOWED_HOSTS' should be a single string of hosts with a space between each.
ALLOWED_HOSTS = os.environ.get("DEVELOPMENT_ALLOWED_HOSTS").split(",")


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',    
    'django.contrib.postgres', # интеграция с PostgreSQL  
    # https://docs.djangoproject.com/en/4.2/ref/contrib/sites/
    'django.contrib.sites',
    # https://docs.djangoproject.com/en/4.2/ref/contrib/sitemaps/
    'django.contrib.sitemaps',
    # https://docs.djangoproject.com/en/4.2/ref/contrib/humanize/
    'django.contrib.humanize', # tempaltes numbers and some dates
]

RECENT_APPS = [
    # https://github.com/un1t/django-cleanup
    'django_cleanup.apps.CleanupConfig',
    # https://django-crispy-forms.readthedocs.io/en/latest/
    'crispy_forms',
    'crispy_bootstrap4',
    # https://django-ckeditor.readthedocs.io/en/latest/
    'ckeditor',
    # https://django-allauth.readthedocs.io/en/latest/
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.github',
    'allauth.socialaccount.providers.google',
    # https://channels.readthedocs.io/en/latest/installation.html
    # 'channels',    
    # https://django-celery-beat.readthedocs.io/en/latest/
    'django_celery_beat',
    # https://django-celery-results.readthedocs.io/en/latest/
    'django_celery_results',

]
INSTALLED_APPS += RECENT_APPS

LOCAL_APPS = [
    'blog.apps.BlogConfig',
    'main_page.apps.MainPageConfig',
    'customer.apps.CustomerConfig',
    'discus.apps.DiscusConfig',
]
INSTALLED_APPS += LOCAL_APPS

# Id Site
SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # Allauth
    # "allauth.account.middleware.AccountMiddleware",
]



ROOT_URLCONF = 'portal.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
            ],
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

# Path where locate error html pages 
ERRORS_TAMPLATES_PATH = 'errors'

WSGI_APPLICATION = 'portal.wsgi.application'


if DEBUG:    
    INTERNAL_IPS = os.getenv('DEBUG_HOSTS').split(",")

    INSTALLED_APPS += [
        'debug_toolbar', # django_debug_toolbar
        'django_extensions',
    ]
    MIDDLEWARE += [
        'debug_toolbar.middleware.DebugToolbarMiddleware'
    ]
    
    DEBUG_TOOLBAR_CONFIG = {
        'SHOW_TOOLBAR_CALLBACK': lambda _request: DEBUG
    }

    
# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': os.getenv('DB_ENGINE'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT'),
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)



# LANGUAGE_CODE = 'ru'


# LANGUAGES = (
#     ('ru', gettext('ru')),
# )



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

# https://docs.djangoproject.com/en/4.2/ref/settings/#static-url
STATIC_URL = 'static/'

# https://docs.djangoproject.com/en/4.2/ref/settings/#static-root
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

# https://docs.djangoproject.com/en/4.2/ref/settings/#staticfiles-dirs
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'other_static/'),
    # os.path.join(BASE_DIR, 'templates/src/')
]

# https://docs.djangoproject.com/en/4.2/ref/settings/#staticfiles-finders
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

# Media files
# https://docs.djangoproject.com/en/4.2/ref/settings/#media-root
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

# https://docs.djangoproject.com/en/4.2/ref/settings/#media-url
MEDIA_URL = 'media/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Start django-crispy-forms
# https://django-crispy-forms.readthedocs.io/en/latest/install.html#installing-django-crispy-forms
# CRISPY_TEMPLATE_PACK = 'uni_form'
CRISPY_TEMPLATE_PACK = 'bootstrap4'
# End django-crispy-forms


# Redirect after login
LOGIN_REDIRECT_URL =  '/'

# django-allauth
# https://django-allauth.readthedocs.io/en/latest/installation.html
AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',
    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
]

SOCIALACCOUNT_PROVIDERS = {
    "github": {
        # Для каждого поставщика вы можете выбрать, должны ли 
        # адреса электронной почты, полученные от поставщика? интерпретироваться как проверенные.
        "VERIFIED_EMAIL": True
    },
    "google": {
        # Для каждого поставщика на основе OAuth либо добавьте `SocialApp`
        # (приложение `socialaccount`), содержащее необходимые учетные данные клиента
        #, или перечислите их здесь:
        "APP": {
            "client_id": "123",
            "secret": "456",
            "key": ""
        },
        # Это настройки конкретного поставщика, которые могут быть
        # перечислены только здесь:
        "SCOPE": [
            "profile",
             "email",
        ],
        "AUTH_PARAMS": {
            "access_type": "online",
        }
    }
}
# End django-allauth

# Sart django-ckeditor
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Custom',
        'toolbar_Custom': [
            ['Bold', 'Italic', 'Underline'],
            ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'],
            ['Link', 'Unlink'],
            ['RemoveFormat', 'Source']
        ]
    },
    'admin_post': {
        'toolbar': 'full',
        'height': 300,
        'width': 800,
    },
}
# End django-ckeditor

# Email
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = os.getenv('EMAIL_PORT')
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS = True

# End Email

# Google Secret Key
GOOGLE_RECAPTCHA_SECRET_KEY = '6LdqzjEUAAAAAKTDYsfuwZce-oa214GC8QeChVBF'

# Message
MESSAGE_TAGS = {
    messages.INFO: 'alert-secondary',
    messages.DEBUG: 'alert-info',
    messages.SUCCESS: 'alert-success',
    messages.WARNING: 'aletr-warning',
    messages.ERROR: 'alert-danger',
}
# End message


# Taggit
# TAGGIT_CASE_INSENSITIVE = True
# End taggit

# Contance
CONSTANCE_BACKEND = 'constance.backends.database.DatabaseBackend'

# CONSTANCE_REDIS_CONNECTION = {
#     'host': 'localhost',
#     'port': 6379,
#     'db': 0,
# }
# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
#         'LOCATION': '127.0.0.1:11211',
#     }
# }
# CONSTANCE_DATABASE_CACHE_BACKEND = 'default'