from django.urls import path
from . import views

app_name = 'ads'

urlpatterns = [
    # Main list views
    path('', views.AutoListView.as_view(), name='autos'),  # The main page for the app
    path('makes', views.MakeListView.as_view(), name='makes'),

    # Auto CRUD
    path('auto_create', views.AutoCreateView.as_view(), name='auto_create'),
    path('auto_update/<int:pk>', views.AutoUpdateView.as_view(), name='auto_update'),
    path('auto_delete/<int:pk>', views.AutoDeleteView.as_view(), name='auto_delete'),

    # Make CRUD
    path('make_create', views.MakeCreateView.as_view(), name='make_create'),
    path('make_update/<int:pk>', views.MakeUpdateView.as_view(), name='make_update'),
    path('make_delete/<int:pk>', views.MakeDeleteView.as_view(), name='make_delete'),

    # The original "Ad" routes from the other app functionality
    path('ad_list', views.AdListView.as_view(), name='all'),
    path('ad_detail/<int:pk>', views.AdDetailView.as_view(), name='ad_detail'),
    path('ad_create', views.AdCreateView.as_view(), name='ad_create'),
    path('ad_update/<int:pk>', views.AdUpdateView.as_view(), name='ad_update'),
    path('ad_delete/<int:pk>', views.AdDeleteView.as_view(), name='ad_delete'),
    path('ad_picture/<int:pk>', views.stream_file, name='ad_picture'),
    path('ad_comment_create/<int:pk>', views.CommentCreateView.as_view(), name='ad_comment_create'),
    path('ad_comment_delete/<int:pk>', views.CommentDeleteView.as_view(), name='ad_comment_delete'),
    path('ad_favorite/<int:pk>', views.AddFavoriteView.as_view(), name='ad_favorite'),
    path('ad_unfavorite/<int:pk>', views.DeleteFavoriteView.as_view(), name='ad_unfavorite'),
]
