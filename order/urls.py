from django.urls import path
from . import views
urlpatterns = [
    path('', views.user_cart, name='user-cart-page'),
    path('add_to_basket', views.add_product_to_basket, name='add-product-to-basket'),
    path('change-count', views.change_count, name='change-product-count'),
    path('remove-product', views.remove_product_from_order_list, name='remove-product'),
]