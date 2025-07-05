from django.urls import path
from . import views

app_name = 'ads'
urlpatterns = [
    path('', views.AdListView.as_view(), name='all'),
    path('simple/', views.simple_ads_list, name='simple_list'),
    path('ad/<int:pk>/', views.AdDetailView.as_view(), name='ad_detail'),
    path('ad/<int:pk>', views.AdDetailView.as_view(), name='ad_detail_no_slash'),
    path('test/<int:pk>/', views.test_detail, name='test_detail'),
    path('simple/<int:pk>/', views.simple_detail, name='simple_detail'),
    path('debug/<int:pk>/', views.debug_detail, name='debug_detail'),
    path('ad/create/', views.AdCreateView.as_view(), name='ad_create'),
    path('ad/<int:pk>/update/', views.AdUpdateView.as_view(), name='ad_update'),
    path('ad/<int:pk>/delete/', views.AdDeleteView.as_view(), name='ad_delete'),
    path('ad/list/ajax/', views.ad_list_ajax, name='ad_list_ajax'),
] 