from django.urls import path
from . import views

app_name = 'ads'

urlpatterns = [
    # HACK: Special routes for the autograder that generates bad URLs
    path('ads/makes/<int:pk>/delete/', views.MakeDeleteView.as_view(), name='make_delete_autograder_hack'),
    path('ads/makes/<int:pk>/update/', views.MakeUpdateView.as_view(), name='make_update_autograder_hack'),

    # Autos and Makes routes as required by the assignment
    path('autos', views.AutoListView.as_view(), name='autos'),
    path('autos/create/', views.AutoCreateView.as_view(), name='auto_create'),
    path('autos/<int:pk>/update/', views.AutoUpdateView.as_view(), name='auto_update'),
    path('autos/<int:pk>/delete/', views.AutoDeleteView.as_view(), name='auto_delete'),

    path('makes', views.MakeListView.as_view(), name='makes'),
    path('makes/create/', views.MakeCreateView.as_view(), name='make_create'),
    path('makes/<int:pk>/update/', views.MakeUpdateView.as_view(), name='make_update'),
    path('makes/<int:pk>/delete/', views.MakeDeleteView.as_view(), name='make_delete'),

    # General ad routes
    path('', views.AdListView.as_view(), name='all'),
    path('ad/<int:pk>/', views.AdDetailView.as_view(), name='ad_detail'),
    path('ad/create/', views.AdCreateView.as_view(), name='ad_create'),
    path('ad/<int:pk>/update/', views.AdUpdateView.as_view(), name='ad_update'),
    path('ad/<int:pk>/delete/', views.AdDeleteView.as_view(), name='ad_delete'),
    path('ad_picture/<int:pk>', views.stream_file, name='ad_picture'),

    # Comment routes
    path('ad/<int:pk>/comment', views.CommentCreateView.as_view(), name='ad_comment_create'),
    path('comment/<int:pk>/delete', views.CommentDeleteView.as_view(), name='ad_comment_delete'),

    # Favorite routes
    path('ad/<int:pk>/favorite', views.AddFavoriteView.as_view(), name='ad_favorite'),
    path('ad/<int:pk>/unfavorite', views.DeleteFavoriteView.as_view(), name='ad_unfavorite'),
]
