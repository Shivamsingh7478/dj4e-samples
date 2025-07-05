#!/usr/bin/env python
import os
import sys
import django

# Add the project directory to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Set up Django with production settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'production_settings')
django.setup()

from django.contrib.auth.models import User

def create_superuser():
    print("Creating superuser account...")
    
    # Check if superuser already exists
    if User.objects.filter(is_superuser=True).exists():
        print("Superuser already exists!")
        superuser = User.objects.filter(is_superuser=True).first()
        print(f"Username: {superuser.username}")
        print(f"Email: {superuser.email}")
        return
    
    # Create superuser
    username = 'admin'
    email = 'admin@example.com'
    password = 'admin123'
    
    try:
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            is_staff=True,
            is_superuser=True
        )
        print(f"Superuser created successfully!")
        print(f"Username: {username}")
        print(f"Email: {email}")
        print(f"Password: {password}")
        print(f"\nYou can now login at: https://shivamsingh747804.pythonanywhere.com/admin/")
        
    except Exception as e:
        print(f"Error creating superuser: {e}")

if __name__ == '__main__':
    create_superuser() 