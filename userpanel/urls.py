from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_dashboard, name='dashboard-page'),
    path('change-password', views.ChangePassword.as_view(), name='change-password-page'),
    path('Edit-profile', views.EditProfile.as_view(), name='edit-profile-info-page'),
]