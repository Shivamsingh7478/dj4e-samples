#!/usr/bin/env python
import os
import sys
import django

sys.path.append('.')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'production_settings')
django.setup()

from ads.models import Ad
from django.contrib.auth.models import User
from django.test import RequestFactory
from ads.views import AdDetailView
from django.urls import reverse

print("=== DEBUGGING DETAIL PAGE ISSUE ===")

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

# Test URL pattern
print(f"\n3. URL Pattern Test:")
try:
    url = reverse('ads:ad_detail', kwargs={'pk': 1})
    print(f"✓ URL pattern works: {url}")
except Exception as e:
    print(f"✗ URL pattern error: {e}")

# Test view
print(f"\n4. View Test:")
factory = RequestFactory()
request = factory.get('/ads/ad/1/')
view = AdDetailView()
view.kwargs = {'pk': 1}
view.request = request

try:
    queryset = view.get_queryset()
    print(f"✓ View queryset works, found {queryset.count()} ads")
    
    obj = view.get_object()
    print(f"✓ View get_object works: '{obj.title}'")
except Exception as e:
    print(f"✗ View error: {e}")

# Test template rendering
print(f"\n5. Template Test:")
try:
    from django.template.loader import render_to_string
    html = render_to_string('ads/ad_detail.html', {'ad': ad_1})
    print(f"✓ Template renders {len(html)} characters")
    
    target_title = 'Graphic Design Services: Logos, Flyers, and More'
    if target_title in html:
        print(f"✓ Target title found in template")
    else:
        print(f"✗ Target title NOT found in template")
        print("Template preview:")
        print(html[:500])
        
except Exception as e:
    print(f"✗ Template error: {e}")

print(f"\n=== END DEBUG ===") 