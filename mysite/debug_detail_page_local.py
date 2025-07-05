#!/usr/bin/env python
import os
import sys
import django

sys.path.append('.')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

from ads.models import Ad
from django.contrib.auth.models import User

print("=== DEBUGGING DETAIL PAGE ISSUE (LOCAL) ===")

# Check database
print("\n1. Database Check:")
ads = Ad.objects.all()
print(f"Total ads: {ads.count()}")
for ad in ads:
    print(f"  - ID: {ad.id}, Title: '{ad.title}', Owner: {ad.owner.username if ad.owner else 'None'}")

# Check specific ad ID 1
print(f"\n2. Ad ID 1 Check:")
try:
    ad_1 = Ad.objects.get(id=1)
    print(f"✓ Ad ID 1 exists: '{ad_1.title}'")
    print(f"  - Owner: {ad_1.owner.username if ad_1.owner else 'None'}")
    print(f"  - Price: {ad_1.price}")
    print(f"  - Text: {ad_1.text[:100]}...")
except Ad.DoesNotExist:
    print("✗ Ad ID 1 does NOT exist")

# Check if the target title exists anywhere
print(f"\n3. Target Title Search:")
target_title = 'Graphic Design Services: Logos, Flyers, and More'
matching_ads = Ad.objects.filter(title=target_title)
print(f"Ads with target title: {matching_ads.count()}")
for ad in matching_ads:
    print(f"  - ID: {ad.id}, Title: '{ad.title}'")

print(f"\n=== END DEBUG ===") 