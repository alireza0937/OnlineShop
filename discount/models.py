from django.db import models
from account.models import User
from product.models import ProductCategory


class DiscountCode(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    code = models.CharField(max_length=15)
    discount_percentage = models.FloatField()
    is_active = models.BooleanField()

    def __str__(self):
        return str(self.is_active)



