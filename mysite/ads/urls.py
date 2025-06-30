from django.urls import path
from . import views

app_name = 'ads'

urlpatterns = [
    path('', views.AutoListView.as_view(), name='autos'),
    path('auto/create/', views.AutoCreateView.as_view(), name='auto_create'),
    path('auto/<int:pk>/update/', views.AutoUpdateView.as_view(), name='auto_update'),
    path('auto/<int:pk>/delete/', views.AutoDeleteView.as_view(), name='auto_delete'),

    path('makes', views.MakeListView.as_view(), name='makes'),
    path('make/create/', views.MakeCreateView.as_view(), name='make_create'),
    path('make/<int:pk>/update/', views.MakeUpdateView.as_view(), name='make_update'),
    path('make/<int:pk>/delete/', views.MakeDeleteView.as_view(), name='make_delete'),

    path('ad/<int:pk>/', views.AdDetailView.as_view(), name='ad_detail'),
    path('ad/create/', views.AdCreateView.as_view(), name='ad_create'),
    path('ad/<int:pk>/update/', views.AdUpdateView.as_view(), name='ad_update'),
    path('ad/<int:pk>/delete/', views.AdDeleteView.as_view(), name='ad_delete'),
    path('ad_picture/<int:pk>', views.stream_file, name='ad_picture'),
    path('ad/<int:pk>/comment', views.CommentCreateView.as_view(), name='ad_comment_create'),
    path('comment/<int:pk>/delete', views.CommentDeleteView.as_view(), name='ad_comment_delete'),
    path('ad/<int:pk>/favorite',
        views.AddFavoriteView.as_view(), name='ad_favorite'),
    path('ad/<int:pk>/unfavorite',
        views.DeleteFavoriteView.as_view(), name='ad_unfavorite'),
]
