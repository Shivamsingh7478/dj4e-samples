from ads.owner import OwnerListView, OwnerDetailView, OwnerCreateView, OwnerUpdateView, OwnerDeleteView
from .models import Ad
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.template.loader import render_to_string

from .forms import CreateForm

class AdListView(OwnerListView):
    model = Ad
    template_name = "ads/ad_list.html"

    def get_queryset(self):
        return Ad.objects.all()

class AdDetailView(OwnerDetailView):
    model = Ad
    template_name = "ads/ad_detail.html"

class AdCreateView(CreateView):
    model = Ad
    fields = ['title', 'price', 'text']
    template_name = "ads/ad_form.html"
    success_url = reverse_lazy('ads:all')
    
    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.owner = self.request.user
        # If not authenticated, owner will be None (which is allowed by the model)
        return super().form_valid(form)

class AdUpdateView(LoginRequiredMixin, UpdateView):
    model = Ad
    fields = ['title', 'price', 'text']
    template_name = "ads/ad_form.html"
    success_url = reverse_lazy('ads:all')

class AdDeleteView(LoginRequiredMixin, DeleteView):
    model = Ad
    template_name = "ads/ad_confirm_delete.html"
    success_url = reverse_lazy('ads:all')

def ad_list_ajax(request):
    """AJAX endpoint to return just the table rows for dynamic updates"""
    ads = Ad.objects.all()
    html = render_to_string('ads/ad_list_rows.html', {'ad_list': ads, 'user': request.user})
    return HttpResponse(html) 