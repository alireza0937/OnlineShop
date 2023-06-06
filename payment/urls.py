from django.urls import path
from . import views
urlpatterns = [
    path('', views.CheckoutView.as_view(), name='checkout-page'),
    path('terms-and-conditions', views.terms_and_conditions, name='terms-and-conditions-page'),
]