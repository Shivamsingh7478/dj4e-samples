#!/usr/bin/env python
import os
import sys
import django

# Add the project directory to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

from django.contrib.auth.models import User
from ads.models import Ad

def create_test_data():
    print("Creating test data...")
    
    # Create or get the autograder user
    username = 'dj4e_user1'
    try:
        user = User.objects.get(username=username)
        print(f"Found existing user: {username}")
    except User.DoesNotExist:
        user = User.objects.create_user(
            username=username,
            password='Meow_5a9bae_41',
            email='dj4e_user1@example.com'
        )
        print(f"Created new user: {username}")
    
    # Create test ad if it doesn't exist
    ad_title = 'Silver Bracelet with Heart Charm'
    try:
        ad = Ad.objects.get(title=ad_title)
        print(f"Found existing ad: {ad_title}")
    except Ad.DoesNotExist:
        ad = Ad.objects.create(
            title=ad_title,
            price=299.99,
            text='Beautiful silver bracelet with heart charm. Perfect gift!',
            owner=user
        )
        print(f"Created new ad: {ad_title}")
    
    # Print all ads
    print("\nAll ads in database:")
    for ad in Ad.objects.all():
        print(f"ID: {ad.id}, Title: {ad.title}")
    
    print(f"\nTest URL should now work: https://shivamsingh747804.pythonanywhere.com/ads/test/{ad.id}/")

if __name__ == '__main__':
    create_test_data() 