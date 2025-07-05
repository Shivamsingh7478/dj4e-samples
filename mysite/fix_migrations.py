#!/usr/bin/env python
import os
import sys
import django

# Add the project directory to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Set up Django with minimal settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'minimal_settings')
django.setup()

def create_missing_migrations():
    print("Creating missing migration files...")
    
    # Create the missing 0003_ad_tags.py migration
    migration_3_content = '''# Generated manually to fix missing migration

from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0002_alter_ad_owner'),
    ]

    operations = [
        # This migration was missing, creating empty migration
    ]
'''
    
    # Create the missing 0004_make_auto.py migration
    migration_4_content = '''# Generated manually to fix missing migration

from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0003_ad_tags'),
    ]

    operations = [
        # This migration was missing, creating empty migration
    ]
'''
    
    # Write the migration files
    with open('ads/migrations/0003_ad_tags.py', 'w') as f:
        f.write(migration_3_content)
    
    with open('ads/migrations/0004_make_auto.py', 'w') as f:
        f.write(migration_4_content)
    
    print("Missing migration files created successfully!")

if __name__ == '__main__':
    create_missing_migrations() 