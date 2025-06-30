from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.
def owner(request: HttpRequest) -> HttpResponse:
    response = HttpResponse()
    response.write("Hello, world. 5fc4279e is the polls index.")
    return response 