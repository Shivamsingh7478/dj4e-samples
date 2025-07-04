from django.http import HttpResponse

def index(request):
    return HttpResponse("Cats app is working!") 