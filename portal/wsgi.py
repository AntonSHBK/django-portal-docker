import os
import sys
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portal.settings')

application = get_wsgi_application()

# if os.environ.get('DEBUG', False):
#     from django.core.management import execute_from_command_line
#     execute_from_command_line(sys.argv)