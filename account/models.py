from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    avatar = models.ImageField(upload_to='users/', blank=True)
    about_user = models.TextField(blank=True)
    email_activation_code = models.CharField(max_length=200)
    address = models.TextField(blank=True)

    def __str__(self):
        return self.username
