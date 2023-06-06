from django.db import models
from account.models import User
from product.models import Product


class WishList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name_plural = 'WishList'


class WishlistDetails(models.Model):
    order = models.ForeignKey(WishList, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.BigIntegerField()

    def __str__(self):
        return str(self.product)

    class Meta:
        verbose_name_plural = 'WishlistDetails'

