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
import os
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.views.static import serve
from django.views.generic import TemplateView
from ads.models import Ad
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login

def custom_login(request, *args, **kwargs):
    ads = Ad.objects.all()
    latest_ad = request.session.get('latest_created_ad')
    form = AuthenticationForm(request, data=request.POST or None)
    
    if request.method == 'POST':
        if request.POST.get('form_type') == 'create_ad':
            # Create the ad
            new_ad = Ad.objects.create(
                title=request.POST.get('title', ''),
                price=request.POST.get('price', ''),
                text=request.POST.get('text', ''),
                owner=request.user if request.user.is_authenticated else None
            )
            # Store the latest created ad in session
            request.session['latest_created_ad'] = {
                'id': new_ad.id,
                'title': new_ad.title,
                'price': str(new_ad.price),
                'text': new_ad.text
            }
            return redirect('/accounts/login/')
        elif form.is_valid():
            auth_login(request, form.get_user())
            return redirect('/')
    
    context = {'form': form, 'ads': ads, 'latest_ad': latest_ad}
    return render(request, 'registration/login.html', context)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('accounts/login/', custom_login, name='login'),
    path('accounts/', include('django.contrib.auth.urls')),
    re_path(r'^oauth/', include('social_django.urls', namespace='social')),
    path('ads/', include('ads.urls')),
]

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
urlpatterns += [
    re_path(r'^site/(?P<path>.*)$', serve,
        {'document_root': os.path.join(BASE_DIR, 'site'),
         'show_indexes': True},
        name='site_path'
        ),
]

urlpatterns += [
    path('favicon.ico', serve, {
            'path': 'favicon.ico',
            'document_root': os.path.join(BASE_DIR, 'home/static'),
        }
    ),
]

try:
    from . import github_settings
    social_login = 'registration/login_social.html'
    urlpatterns.insert(0,
                       path('accounts/login/', auth_views.LoginView.as_view(template_name=social_login))
                       )
    print('Using', social_login, 'as the login template')
except:
    print('Using registration/login.html as the login template')
