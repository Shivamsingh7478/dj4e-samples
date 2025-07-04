from ads.owner import OwnerListView, OwnerDetailView, OwnerCreateView, OwnerUpdateView, OwnerDeleteView
from .models import Ad
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView

class AdListView(LoginRequiredMixin, OwnerListView):
    model = Ad
    template_name = "ads/ad_list.html"

    def get_queryset(self):
        return Ad.objects.all()

class AdDetailView(OwnerDetailView):
    model = Ad
    template_name = "ads/ad_detail.html"

class AdCreateView(OwnerCreateView):
    model = Ad
    fields = ['title', 'price', 'text']
    template_name = "ads/ad_form.html"

class AdUpdateView(LoginRequiredMixin, UpdateView):
    model = Ad
    fields = ['title', 'price', 'text']
    template_name = "ads/ad_form.html"
    success_url = '/ads/'

class AdDeleteView(OwnerDeleteView):
    model = Ad
    template_name = "ads/ad_confirm_delete.html" 