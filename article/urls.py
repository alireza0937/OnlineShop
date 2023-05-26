from django.urls import path
from . import views

urlpatterns = [

    path('', views.BlogListView.as_view(), name='blog-page'),
    path('tags/<tag>', views.BlogListView.as_view(), name='blog-list-by-tag-page'),
    path('categories/<cat>', views.BlogListView.as_view(), name='blog-list-by-categories-page'),
    path('<pk>', views.BlogDetailView.as_view(), name='blog-detail-page'),


]
