"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse

def redirect_to_ads(request):
    return redirect('ads:all')

def favicon(request):
    # Return a simple favicon response
    return HttpResponse(
        b'\x00\x00\x01\x00\x01\x00\x10\x10\x00\x00\x01\x00\x20\x00\x68\x04\x00\x00\x16\x00\x00\x00',
        content_type='image/x-icon'
    )

# Django Tutorial 01 Assignment View
def tutorial01_index(request):
    return HttpResponse("Hello, world. 52883377 is the polls index.")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', redirect_to_ads, name='home'),
    # path('home/', include('home.urls')),  # Commented out to avoid import issues
    path('tutorial01/', tutorial01_index, name='tutorial01_index'),
    path('ads/', include('ads.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('oauth/', include('social_django.urls', namespace='social')),
    path('favicon.ico', favicon, name='favicon'),
]

# Add static files serving for development and production
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
