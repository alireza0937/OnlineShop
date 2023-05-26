from django.db import models
from django.utils.text import slugify
from account.models import User


class ProductCategory(models.Model):
    Parent = models.ForeignKey('ProductCategory', on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    url_title = models.CharField(max_length=200)
    is_active = models.BooleanField()

    class Meta:
        verbose_name_plural = 'ProductsCategories'

    def __str__(self):
        return self.title


class ProductBrand(models.Model):
    title = models.CharField(max_length=200)
    url_title = models.CharField(max_length=200)
    is_active = models.BooleanField()

    class Meta:
        verbose_name_plural = 'ProductsBrand'

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=250)
    brand = models.ForeignKey(ProductBrand, on_delete=models.CASCADE, null=False)
    category = models.ManyToManyField(ProductCategory)
    image = models.ImageField(upload_to='product/')
    short_descriptions = models.CharField(max_length=500, null=True, db_index=True)
    price = models.CharField(max_length=250)
    description = models.TextField()
    slug = models.SlugField(unique=True, editable=False, db_index=True, max_length=200)
    is_new = models.BooleanField()
    is_active = models.BooleanField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Product, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.title


class ProductVisit(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.product)

    class Meta:
        verbose_name_plural = 'ProductsVisits'
