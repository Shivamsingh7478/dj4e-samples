from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

from .models import Question

# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def owner(request: HttpRequest) -> HttpResponse:
    response = HttpResponse()
    response.write("Hello, world. 5fc4279e is the polls index.")
    return response 