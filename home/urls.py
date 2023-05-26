from django.urls import path
from . import views
urlpatterns = [
    path('', views.HomeView.as_view(), name='index-page'),
    path('aboutus/', views.about_us, name='aboutUs-page'),
    path('contact-us/', views.ContactUs.as_view(), name='contact-page'),

]