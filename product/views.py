from django.db.models import Count
from django.http import HttpRequest
from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from product.models import Product, ProductCategory, ProductBrand, ProductVisit
from sitesetting.models import Advertising


class ProductListView(ListView):
    model = Product
    template_name = 'product/product_list.html'
    context_object_name = 'products'
    paginate_by = 9

    def get_queryset(self):
        query = super().get_queryset()
        chosen_category = self.kwargs.get('cat')
        searched_product = self.request.GET.get('search')
        chosen_brand = self.kwargs.get('brand')
        if chosen_category is not None:
            Product.objects.filter(category__url_title__iexact=chosen_category)
            query = query.filter(category__url_title__iexact=chosen_category)
        if chosen_brand is not None:
            query = query.filter(brand__url_title=chosen_brand)

        if searched_product is not None:
            query = query.filter(title__icontains=searched_product)
        return query

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductListView, self).get_context_data()
        context['adv_irancell'] = Advertising.objects.filter(position__iexact=Advertising.BannerPosition.product_list,
                                                             title='ایرانسل').first()
        context['adv_mci'] = Advertising.objects.filter(position__iexact=Advertising.BannerPosition.product_list,
                                                        title='همراه اول').first()
        return context


def product_detail(request: HttpRequest, slug):
    user = request.user.id
    chosen_product = Product.objects.filter(slug=slug).first()

    if user is not None:
        visit = ProductVisit(product_id=chosen_product.id, user_id=request.user.id)
        visit.save()
    else:
        visit = ProductVisit(product_id=chosen_product.id)
        visit.save()
    related_product = Product.objects.filter(brand=chosen_product.brand).exclude(pk=chosen_product.id)[:4]
    return render(request, 'product/product_details.html', context={
        'products': chosen_product,
        'related_product': related_product
    })


def product_categories(request: HttpRequest):
    all_categories = ProductCategory.objects.annotate(category_count=Count('url_title')).filter(Parent_id=None)
    return render(request, 'product/components/categories.html', context={
        'all_categories': all_categories
    })


def product_brands(request: HttpRequest):
    all_brands = ProductBrand.objects.annotate(brand_count=Count("product")).all()
    return render(request, 'product/components/brand.html', context={
        'all_brands': all_brands
    })


class AllCategories(TemplateView):
    template_name = 'product/all_categories.html'

    def get_context_data(self, **kwargs):
        context = super(AllCategories, self).get_context_data()
        context['main_categories'] = ProductCategory.objects.filter(Parent=None).all()
        return context
