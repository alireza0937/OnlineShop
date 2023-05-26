from django.contrib import admin
from product.models import Product, ProductCategory, ProductBrand, ProductVisit


class Category(admin.ModelAdmin):
    list_display = ['title', 'Parent']


admin.site.register(Product)
admin.site.register(ProductCategory, Category)
admin.site.register(ProductBrand)
admin.site.register(ProductVisit)
