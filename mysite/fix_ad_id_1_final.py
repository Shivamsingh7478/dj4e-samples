#!/usr/bin/env python
import os
import sys
import django

sys.path.append('.')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'production_settings')
django.setup()

from ads.models import Ad
from django.contrib.auth.models import User

print("=== FIXING AD ID 1 - FINAL SOLUTION ===")

# Step 1: Check current state
print("\n1. Current database state:")
ads = Ad.objects.all()
print(f"Total ads: {ads.count()}")
for ad in ads:
    print(f"  - ID: {ad.id}, Title: '{ad.title}', Owner: {ad.owner.username if ad.owner else 'None'}")

# Step 2: Create user if needed
print("\n2. Creating/fixing user...")
user, created = User.objects.get_or_create(
    username='dj4e_user1',
    defaults={
        'email': 'dj4e_user1@example.com',
        'password': 'Meow_dee7f5_41'
    }
)

if created:
    print(f"Created user: {user.username}")
else:
    print(f"Found existing user: {user.username}")
    user.set_password('Meow_dee7f5_41')
    user.save()
    print("Reset password to 'Meow_dee7f5_41'")

# Step 3: Delete existing ad with ID 5 (wrong one)
print("\n3. Cleaning up wrong ads...")
Ad.objects.filter(id=5).delete()
print("Deleted ad ID 5")

# Step 4: Create ad with ID 1 (the one autograder needs)
print("\n4. Creating ad ID 1...")
ad_1 = Ad.objects.create(
    id=1,
    title='Graphic Design Services: Logos, Flyers, and More',
    price=150.00,
    text='Professional graphic design services including logos, flyers, business cards, and more. High quality work at competitive prices.',
    owner=user
)
print(f"✓ Created ad ID 1: '{ad_1.title}'")

# Step 5: Create ad with ID 2
print("\n5. Creating ad ID 2...")
ad_2 = Ad.objects.create(
    id=2,
    title='Silver Bracelet with Heart Charm',
    price=299.99,
    text='Beautiful silver bracelet with heart charm. Perfect gift!',
    owner=user
)
print(f"✓ Created ad ID 2: '{ad_2.title}'")

# Step 6: Final verification
print("\n6. Final verification:")
final_ads = Ad.objects.all()
print(f"Total ads: {final_ads.count()}")
for ad in final_ads:
    print(f"  - ID: {ad.id}, Title: '{ad.title}', Owner: {ad.owner.username}")

print(f"\n=== FIX COMPLETE ===")
print("Now test these URLs:")
print(f"  - Debug: https://shivamsingh747804.pythonanywhere.com/ads/debug/1/")
print(f"  - Detail: https://shivamsingh747804.pythonanywhere.com/ads/ad/1/")
print(f"  - Simple: https://shivamsingh747804.pythonanywhere.com/ads/simple/1/")
print(f"  - Test: https://shivamsingh747804.pythonanywhere.com/ads/test/1/") 