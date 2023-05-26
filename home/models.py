from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


# Create your models here.

class ContactUs(models.Model):
    subject = models.CharField(max_length=500)
    name = models.CharField(max_length=300)
    email = models.EmailField()
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    response = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = 'ContactUs'

    def __str__(self):
        return self.subject
