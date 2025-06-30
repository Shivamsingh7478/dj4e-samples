from django.shortcuts import render
from django.views import View
from django.conf import settings
from django.http import HttpResponse

# Create your views here.

# This is a little complex because we need to detect when we are
# running in various configurations

# Django Tutorial 01 Assignment View
def tutorial01_index(request):
    return HttpResponse("Hello, world. 52883377 is the polls index.")

class HomeView(View):
    def get(self, request):
        print(request.get_host())
        host = request.get_host()
        islocal = host.find('localhost') >= 0 or host.find('127.0.0.1') >= 0
        context = {
            'installed': settings.INSTALLED_APPS,
            'islocal': islocal
        }
        return render(request, 'home/main.html', context)
