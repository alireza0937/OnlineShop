from django.db import models
from account.models import User
from product.models import Product


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_paid = models.BooleanField(default=False)
    total_price = models.BigIntegerField(blank=True, null=True)
    payment_date = models.DateField(blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Orders'

    def __str__(self):
        return str(self.user)

    def calculate_basket_total_price(self):
        total = 0
        for orders in self.orderdetail_set.all():
            total += orders.final_price
        return total


class OrderDetail(models.Model):
    orderby = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    count = models.IntegerField()
    final_price = models.BigIntegerField(blank=True, null=True)

    class Meta:
        verbose_name_plural = 'OrderDetails'

    def __str__(self):
        return str(self.product)

    def calculate_each_product_price(self):
        return int(self.product.price) * int(self.count)
