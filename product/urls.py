from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.ProductListView.as_view(), name='product-list-page'),
    path('products/categories/<cat>/', views.ProductListView.as_view(), name='product-by-categories-page'),
    path('products/brands/<brand>/', views.ProductListView.as_view(), name='product-by-brands-page'),
    path('products/<slug:slug>', views.product_detail, name='product-detail-page'),
    path('allcategories', views.AllCategories.as_view(), name='all-categories-page'),

]
