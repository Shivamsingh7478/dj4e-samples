#!/usr/bin/env python3
"""
Simple script to check if the required ad exists
"""
import os
import sys
import django

# Add the project directory to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

from ads.models import Ad

def check_ads():
    print("Checking ads in database...")
    
    # Get all ads
    ads = Ad.objects.all()
    print(f"Total ads in database: {ads.count()}")
    
    # Look for the specific ad
    target_title = "Graphic Design Services: Logos, Flyers, and More"
    target_ad = None
    
    for ad in ads:
        print(f"Ad ID {ad.id}: '{ad.title}' (Owner: {ad.owner.username if ad.owner else 'None'})")
        if ad.title == target_title:
            target_ad = ad
    
    if target_ad:
        print(f"\n✅ FOUND TARGET AD:")
        print(f"   ID: {target_ad.id}")
        print(f"   Title: '{target_ad.title}'")
        print(f"   Price: ${target_ad.price}")
        print(f"   Owner: {target_ad.owner.username if target_ad.owner else 'None'}")
        print(f"   URL: /ads/ad/{target_ad.id}/")
    else:
        print(f"\n❌ TARGET AD NOT FOUND: '{target_title}'")
        
        # Check if there are any ads with similar titles
        similar_ads = [ad for ad in ads if 'graphic' in ad.title.lower() or 'design' in ad.title.lower()]
        if similar_ads:
            print("Similar ads found:")
            for ad in similar_ads:
                print(f"   '{ad.title}' (ID: {ad.id})")

if __name__ == '__main__':
    check_ads() 