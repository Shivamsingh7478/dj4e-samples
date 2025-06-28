import os
import sys

# Add your project directory to the sys.path
path = '/home/shivamsingh747804/dj4e-samples/mysite'
if path not in sys.path:
    sys.path.append(path)

# Set the Django settings module
os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

# Serve Django via WSGI
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application() 