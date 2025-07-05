from django.shortcuts import render
from ads.models import Ad
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.http import HttpResponse

def index(request):
    ads = Ad.objects.all()
    return render(request, 'home/main.html', {'ads': ads})

def logout_view(request):
    """Simple logout view"""
    logout(request)
    return HttpResponse("""
    <html>
    <head><title>Logged Out</title></head>
    <body>
        <h1>Logged Out</h1>
        <p>You have been successfully logged out.</p>
        <p><a href="/">Go to Home</a></p>
    </body>
    </html>
    """) 