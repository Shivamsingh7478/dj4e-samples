from django.shortcuts import render
from ads.models import Ad

def index(request):
    ads = Ad.objects.all()
    return render(request, 'home/main.html', {'ads': ads}) 