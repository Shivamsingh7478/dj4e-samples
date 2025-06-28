from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import ListView, DetailView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.db.models import Q

from .models import Ad, Comment, Fav
from .forms import CreateForm, CommentForm

# csrf exemption in class based views
# https://stackoverflow.com/questions/16458166/how-to-disable-djangos-csrf-validation
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.db.utils import IntegrityError

class AdListView(ListView):
    model = Ad
    template_name = 'ads/ad_list.html'
    context_object_name = 'ad_list'

    def get(self, request):
        ad_list = Ad.objects.all()
        search = request.GET.get('search', '')
        if search:
            ad_list = ad_list.filter(
                Q(title__icontains=search) |
                Q(text__icontains=search) |
                Q(tags__icontains=search)
            )
        
        favorites = list()
        if request.user.is_authenticated:
            # rows = [{'id': 2}, {'id': 4} ... ]  (A list of rows)
            rows = request.user.favorite_ads.values('id')
            # favorites = [2, 4, ...] using list comprehension
            favorites = [ row['id'] for row in rows ]
        ctx = {'ad_list': ad_list, 'favorites': favorites, 'search': search}
        return render(request, self.template_name, ctx)

class AdDetailView(View):
    def get(self, request, pk):
        ad = get_object_or_404(Ad, id=pk)
        comments = Comment.objects.filter(ad=ad).order_by('-updated_at')
        comment_form = CommentForm()
        context = {'ad': ad, 'comments': comments, 'comment_form': comment_form}
        return render(request, 'ads/ad_detail.html', context)

class AdCreateView(LoginRequiredMixin, View):
    def get(self, request):
        form = CreateForm()
        return render(request, 'ads/ad_form.html', {'form': form})

    def post(self, request):
        form = CreateForm(request.POST, request.FILES or None)
        if not form.is_valid():
            return render(request, 'ads/ad_form.html', {'form': form})

        ad = form.save(commit=False)
        ad.owner = request.user
        if 'picture' in request.FILES:
            ad.picture = request.FILES['picture'].read()
            ad.content_type = request.FILES['picture'].content_type
        ad.save()
        return redirect('ads:all')

class AdUpdateView(LoginRequiredMixin, View):
    def get(self, request, pk):
        ad = get_object_or_404(Ad, id=pk, owner=request.user)
        form = CreateForm(instance=ad)
        return render(request, 'ads/ad_form.html', {'form': form})

    def post(self, request, pk):
        ad = get_object_or_404(Ad, id=pk, owner=request.user)
        form = CreateForm(request.POST, request.FILES or None, instance=ad)

        if not form.is_valid():
            return render(request, 'ads/ad_form.html', {'form': form})

        ad = form.save(commit=False)
        if 'picture' in request.FILES:
            ad.picture = request.FILES['picture'].read()
            ad.content_type = request.FILES['picture'].content_type
        ad.save()
        return redirect('ads:all')

class AdDeleteView(LoginRequiredMixin, DeleteView):
    model = Ad
    success_url = reverse_lazy('ads:all')
    template_name = 'ads/ad_confirm_delete.html'

def stream_file(request, pk):
    ad = get_object_or_404(Ad, id=pk)
    if not ad.picture:
        raise Http404
    return HttpResponse(ad.picture, content_type=ad.content_type)

class CommentCreateView(LoginRequiredMixin, View):
    def post(self, request, pk):
        ad = get_object_or_404(Ad, id=pk)
        comment = Comment(text=request.POST['comment'], owner=request.user, ad=ad)
        comment.save()
        return redirect('ads:ad_detail', pk=pk)

class CommentDeleteView(LoginRequiredMixin, DeleteView):
    model = Comment
    template_name = 'ads/comment_delete.html'

    def get_success_url(self):
        ad = self.object.ad
        return reverse_lazy('ads:ad_detail', args=[ad.id])

@method_decorator(csrf_exempt, name='dispatch')
class AddFavoriteView(LoginRequiredMixin, View):
    def post(self, request, pk):
        print("Add PK",pk)
        ad = get_object_or_404(Ad, id=pk)
        fav = Fav(user=request.user, ad=ad)
        try:
            fav.save()  # In case of duplicate key
        except IntegrityError:
            pass
        return HttpResponse("Favorite added 42")

@method_decorator(csrf_exempt, name='dispatch')
class DeleteFavoriteView(LoginRequiredMixin, View):
    def post(self, request, pk):
        print("Delete PK",pk)
        ad = get_object_or_404(Ad, id=pk)
        try:
            Fav.objects.get(user=request.user, ad=ad).delete()
        except Fav.DoesNotExist:
            pass

        return HttpResponse("Favorite deleted 42")
