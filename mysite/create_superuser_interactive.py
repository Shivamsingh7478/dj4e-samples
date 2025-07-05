#!/usr/bin/env python
import os
import sys
import django
import getpass

# Add the project directory to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Set up Django with production settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'production_settings')
django.setup()

from django.contrib.auth.models import User

def create_superuser_interactive():
    print("Creating superuser account (interactive mode)...")
    
    # Get user input
    username = input("Enter username: ")
    email = input("Enter email: ")
    password = getpass.getpass("Enter password: ")
    password_confirm = getpass.getpass("Confirm password: ")
    
    if password != password_confirm:
        print("Passwords don't match!")
        return
    
    try:
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            is_staff=True,
            is_superuser=True
        )
        print(f"Superuser '{username}' created successfully!")
        print(f"You can now login at: https://shivamsingh747804.pythonanywhere.com/admin/")
        
    except Exception as e:
        print(f"Error creating superuser: {e}")

if __name__ == '__main__':
    create_superuser_interactive() 