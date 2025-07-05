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
from ads.models import Ad

def add_missing_ad():
    print("Adding missing ad for autograder...")
    
    # Get or create the user
    username = 'dj4e_user1'
    try:
        user = User.objects.get(username=username)
        print(f"Found user: {username}")
    except User.DoesNotExist:
        user = User.objects.create_user(
            username=username,
            password='Meow_dee7f5_41',
            email='dj4e_user1@example.com'
        )
        print(f"Created user: {username}")
    
    # Check if the ad already exists
    ad_title = 'Graphic Design Services: Logos, Flyers, and More'
    try:
        ad = Ad.objects.get(title=ad_title)
        print(f"Ad already exists: {ad_title}")
    except Ad.DoesNotExist:
        # Create the missing ad
        ad = Ad.objects.create(
            title=ad_title,
            price=150.00,
            text='Professional graphic design services including logos, flyers, business cards, and more. High quality work at competitive prices.',
            owner=user
        )
        print(f"Created ad: {ad_title}")
    
    # Print all ads
    print("\nAll ads in database:")
    for ad in Ad.objects.all():
        print(f"ID: {ad.id}, Title: {ad.title}")
    
    print(f"\nAutograder should now find the required ad!")

if __name__ == '__main__':
    add_missing_ad() 