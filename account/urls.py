from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register-page'),
    path('register/<activation_code>', views.authentication, name='authentication-page'),
    path('login/', views.LoginView.as_view(), name='login-page'),
    path('login/exit', views.logout_account, name='logout'),

]