from django.db import models


class SliderSetting(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='sliders/')
    url = models.CharField(max_length=200)
    short_description = models.CharField(max_length=300, default='')
    is_active = models.BooleanField()

    def __str__(self):
        return self.title


class Advertising(models.Model):
    class BannerPosition(models.TextChoices):
        home = 'index-page'
        product_list = 'product-list-page'

    title = models.CharField(max_length=200)
    banner = models.ImageField(upload_to='advertise/')
    url_title = models.URLField()
    position = models.CharField(max_length=200, choices=BannerPosition.choices)

    def __str__(self):
        return self.title
