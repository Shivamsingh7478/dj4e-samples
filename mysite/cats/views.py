from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class CatList(TemplateView):
    template_name = "cats/cat_list.html"
