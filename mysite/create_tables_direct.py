#!/usr/bin/env python
import os
import sys
import django

# Add the project directory to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Set up Django with minimal settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'minimal_settings')
django.setup()

from django.db import connection
from django.core.management import execute_from_command_line

def create_tables_direct():
    print("Creating database tables directly...")
    
    # Create tables using Django's schema creation
    with connection.schema_editor() as schema_editor:
        # Create the ads_ad table
        schema_editor.create_model(Ad)
    
    print("Tables created successfully!")

if __name__ == '__main__':
    # Import the Ad model after Django setup
    from ads.models import Ad
    create_tables_direct() 