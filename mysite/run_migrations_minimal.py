#!/usr/bin/env python
import os
import sys
import django

# Add the project directory to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Set up Django with minimal settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'minimal_settings')
django.setup()

from django.core.management import execute_from_command_line

def run_migrations():
    print("Running migrations with minimal settings...")
    
    # Run migrations
    execute_from_command_line(['manage.py', 'migrate'])
    
    print("Migrations completed successfully!")

if __name__ == '__main__':
    run_migrations() 