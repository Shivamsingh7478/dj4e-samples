from django.http import HttpResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect
from .models import Cat, Breed

def index(request):
    return HttpResponse("Cats app is working!")

# Custom view for /cats/
def cats_root(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request, data=request.POST)
            if form.is_valid():
                auth_login(request, form.get_user())
                return redirect('all')
        else:
            form = AuthenticationForm()
        return render(request, 'cats/login_on_cats.html', {'form': form})
    # If authenticated, show the cat list
    return CatList.as_view()(request)

# Cat Views
class CatList(LoginRequiredMixin, ListView):
    model = Cat
    template_name = 'cats/cat_list.html'
    context_object_name = 'cat_list'

class CatCreate(LoginRequiredMixin, CreateView):
    model = Cat
    fields = '__all__'
    template_name = 'cats/cat_form.html'
    success_url = reverse_lazy('all')

class CatUpdate(LoginRequiredMixin, UpdateView):
    model = Cat
    fields = '__all__'
    template_name = 'cats/cat_form.html'
    success_url = reverse_lazy('all')

class CatDelete(LoginRequiredMixin, DeleteView):
    model = Cat
    template_name = 'cats/cat_confirm_delete.html'
    success_url = reverse_lazy('all')

# Breed Views
class BreedList(LoginRequiredMixin, ListView):
    model = Breed
    template_name = 'cats/breed_list.html'
    context_object_name = 'breed_list'

class BreedCreate(LoginRequiredMixin, CreateView):
    model = Breed
    fields = '__all__'
    template_name = 'cats/breed_form.html'
    success_url = reverse_lazy('breed_list')

class BreedUpdate(LoginRequiredMixin, UpdateView):
    model = Breed
    fields = '__all__'
    template_name = 'cats/breed_form.html'
    success_url = reverse_lazy('breed_list')

class BreedDelete(LoginRequiredMixin, DeleteView):
    model = Breed
    template_name = 'cats/breed_confirm_delete.html'
    success_url = reverse_lazy('breed_list') 