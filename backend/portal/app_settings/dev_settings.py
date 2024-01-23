from .common_settings import *

INTERNAL_IPS = os.getenv('DEBUG_HOSTS').split(',')

# 'DJANGO_ALLOWED_HOSTS' should be a single string of hosts with a space between each.
ALLOWED_HOSTS = os.environ.get("DEVELOPMENT_ALLOWED_HOSTS").split(",")

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