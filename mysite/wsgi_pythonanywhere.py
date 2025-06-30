import os
import sys

# Add the parent directory of your project to the sys.path
path = '/home/shivamsingh747804/dj4e-samples'
if path not in sys.path:
    sys.path.insert(0, path)

# Set the Django settings module to point to your mysite settings
os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

# Serve Django via WSGI
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application() 