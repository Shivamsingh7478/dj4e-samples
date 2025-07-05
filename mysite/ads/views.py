from ads.owner import OwnerListView, OwnerDetailView, OwnerCreateView, OwnerUpdateView, OwnerDeleteView
from .models import Ad
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from django.middleware.csrf import get_token

from .forms import CreateForm

class AdListView(OwnerListView):
    model = Ad
    template_name = "ads/ad_list.html"

    def get_queryset(self):
        return Ad.objects.all()
    
    def get(self, request, *args, **kwargs):
        # First try the normal template-based approach
        try:
            return super().get(request, *args, **kwargs)
        except Exception as e:
            # If template fails, fall back to simple HTML
            ads = Ad.objects.all()
            html = f"""
            <html>
            <head><title>Ads List</title></head>
            <body>
                <h1>Ads List</h1>
                <table border="1" style="width: 100%; border-collapse: collapse;">
                    <thead>
                        <tr>
                            <th>Title</th>
                            <th>Price</th>
                            <th>Actions</th>
                        </tr>
                    </thead>
                    <tbody>
            """
            
            for ad in ads:
                html += f"""
                        <tr>
                            <td><a href="/ads/ad/{ad.id}/">{ad.title}</a></td>
                            <td>${ad.price}</td>
                            <td>
                                <a href="/ads/ad/{ad.id}/update/">Edit</a> | 
                                <a href="/ads/ad/{ad.id}/delete/">Delete</a>
                            </td>
                        </tr>
                """
            
            html += """
                    </tbody>
                </table>
                <p>
                    <a href="/ads/ad/create/">Create Ad</a> |
                    <a href="/ads/">View all</a>
                </p>
            </body>
            </html>
            """
            
            return HttpResponse(html)

def simple_ads_list(request):
    """Simple ads list view that shows all ads"""
    ads = Ad.objects.all()
    html = f"""
    <html>
    <head><title>Ads List</title></head>
    <body>
        <h1>Ads List</h1>
        <table border="1" style="width: 100%; border-collapse: collapse;">
            <thead>
                <tr>
                    <th>Title</th>
                    <th>Price</th>
                    <th>Actions</th>
                </tr>
            </thead>
            <tbody>
    """
    
    for ad in ads:
        html += f"""
                <tr>
                    <td><a href="/ads/ad/{ad.id}/">{ad.title}</a></td>
                    <td>${ad.price}</td>
                    <td>
                        <a href="/ads/ad/{ad.id}/update/">Edit</a> | 
                        <a href="/ads/ad/{ad.id}/delete/">Delete</a>
                    </td>
                </tr>
        """
    
    html += """
            </tbody>
        </table>
        <p>
            <a href="/ads/ad/create/">Create Ad</a> |
            <a href="/ads/">View all</a>
        </p>
    </body>
    </html>
    """
    
    return HttpResponse(html)

class AdDetailView(OwnerDetailView):
    model = Ad
    template_name = "ads/ad_detail.html"
    
    def get_queryset(self):
        return Ad.objects.all()

def debug_detail(request, pk):
    """Debug view to test URL routing and database access"""
    try:
        # Test database access
        ads = Ad.objects.all()
        ad_count = ads.count()
        
        # Try to get specific ad
        try:
            ad = Ad.objects.get(id=pk)
            ad_found = True
            ad_title = ad.title
        except Ad.DoesNotExist:
            ad_found = False
            ad_title = "Not found"
        
        html = f"""
        <html>
        <head><title>Debug - Ad {pk}</title></head>
        <body>
            <h1>Debug Information</h1>
            <p><strong>Requested PK:</strong> {pk}</p>
            <p><strong>Total ads in database:</strong> {ad_count}</p>
            <p><strong>Ad found:</strong> {ad_found}</p>
            <p><strong>Ad title:</strong> {ad_title}</p>
            
            <h2>All ads in database:</h2>
            <ul>
        """
        
        for ad in ads:
            html += f"<li>ID: {ad.id}, Title: '{ad.title}', Owner: {ad.owner.username if ad.owner else 'None'}</li>"
        
        html += """
            </ul>
            
            <h2>Test URLs:</h2>
            <ul>
                <li><a href="/ads/test/1/">Test Detail 1</a></li>
                <li><a href="/ads/simple/1/">Simple Detail 1</a></li>
                <li><a href="/ads/ad/1/">Regular Detail 1</a></li>
            </ul>
        </body>
        </html>
        """
        
        return HttpResponse(html)
        
    except Exception as e:
        return HttpResponse(f"Error in debug view: {e}", status=500)

def simple_detail(request, pk):
    """Simple detail view that should work without complex dependencies"""
    try:
        ad = Ad.objects.get(id=pk)
        html = f"""
        <html>
        <head><title>{ad.title}</title></head>
        <body>
            <h1>{ad.title}</h1>
            <p><strong>Price:</strong> ${ad.price}</p>
            <p><strong>Description:</strong> {ad.text}</p>
            <p><strong>Owner:</strong> {ad.owner.username if ad.owner else 'None'}</p>
            <p><a href="/ads/">Back to Ads List</a></p>
        </body>
        </html>
        """
        return HttpResponse(html)
    except Ad.DoesNotExist:
        return HttpResponse(f"Ad ID {pk} not found", status=404)
    except Exception as e:
        return HttpResponse(f"Error: {e}", status=500)

class AdCreateView(CreateView):
    model = Ad
    form_class = CreateForm
    template_name = "ads/ad_form.html"
    success_url = '/ads/'
    
    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.owner = self.request.user
        else:
            # Create a default user for anonymous ads
            default_user, created = User.objects.get_or_create(
                username='anonymous',
                defaults={'email': 'anonymous@example.com'}
            )
            form.instance.owner = default_user
        return super().form_valid(form)

class AdUpdateView(UpdateView):
    model = Ad
    fields = ['title', 'price', 'text']
    template_name = "ads/ad_form.html"
    success_url = reverse_lazy('ads:all')
    
    def get_queryset(self):
        return Ad.objects.all()

class AdDeleteView(DeleteView):
    model = Ad
    template_name = "ads/ad_confirm_delete.html"
    success_url = reverse_lazy('ads:all')
    
    def get_queryset(self):
        return Ad.objects.all()

def simple_delete(request, pk):
    """Simple delete view that doesn't rely on owner mixin"""
    try:
        ad = Ad.objects.get(id=pk)
        if request.method == 'POST':
            ad.delete()
            return redirect('ads:all')
        
        # Get CSRF token
        csrf_token = get_token(request)
        
        html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Delete Ad</title>
            <meta charset="utf-8">
            <style>
                body {{ font-family: Arial, sans-serif; margin: 50px; }}
                .container {{ max-width: 500px; margin: 0 auto; }}
                .btn {{ 
                    display: inline-block; 
                    padding: 10px 20px; 
                    margin: 5px; 
                    text-decoration: none; 
                    border-radius: 5px; 
                    border: none; 
                    cursor: pointer; 
                }}
                .btn-danger {{ background-color: #dc3545; color: white; }}
                .btn-secondary {{ background-color: #6c757d; color: white; }}
                .btn-primary {{ background-color: #007bff; color: white; }}
                .btn:hover {{ opacity: 0.8; }}
                .links {{ margin-top: 20px; padding-top: 20px; border-top: 1px solid #ddd; }}
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Delete Ad</h1>
                <p>Are you sure you want to delete "{ad.title}"?</p>
                <form method="post">
                    <input type="hidden" name="csrfmiddlewaretoken" value="{csrf_token}">
                    <button type="submit" class="btn btn-danger">Yes, delete.</button>
                    <a href="/ads/" class="btn btn-secondary">Cancel</a>
                </form>
                <div class="links">
                    <a href="/ads/ad/create/" class="btn btn-primary">Create Ad</a> |
                    <a href="/ads/" class="btn btn-secondary">View all</a>
                </div>
            </div>
        </body>
        </html>
        """
        return HttpResponse(html)
        
    except Ad.DoesNotExist:
        return HttpResponse(f"Ad ID {pk} not found", status=404)
    except Exception as e:
        return HttpResponse(f"Error: {e}", status=500)

def test_detail(request, pk):
    """Simple test view to debug the detail page issue"""
    try:
        ad = Ad.objects.get(id=pk)
        return HttpResponse(f"Test: Found ad ID {pk} - {ad.title}")
    except Ad.DoesNotExist:
        return HttpResponse(f"Test: Ad ID {pk} not found")
    except Exception as e:
        return HttpResponse(f"Test: Error - {e}")

def ad_list_ajax(request):
    """AJAX endpoint to return just the table rows for dynamic updates"""
    ads = Ad.objects.all()
    html = render_to_string('ads/ad_list_rows.html', {'ad_list': ads, 'user': request.user})
    return HttpResponse(html) 