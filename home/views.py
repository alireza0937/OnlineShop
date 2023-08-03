from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView
from account.models import User
from home.forms import ContactUsModelForm
from product.models import ProductVisit, Product, ProductCategory, ProductBrand
from sitesetting.models import SliderSetting, Advertising


class HomeView(TemplateView):
    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data()
        context['most_visit_products'] = ProductVisit.objects.raw(
            "select p.title, (pv.product_id), count(pv.product_id), 1 as id "
            "from product_product as p "
            "inner join product_productvisit as pv "
            "on p.id = pv.product_id "
            "group by p.title,pv.product_id")[:6]
        context['slider'] = SliderSetting.objects.filter(is_active=True).all()
        context['adv_ewano'] = Advertising.objects.filter(position__iexact=Advertising.BannerPosition.home,
                                                          title='اوانو').first()

        context['adv_last_sec'] = Advertising.objects.filter(position__iexact=Advertising.BannerPosition.home,
                                                             title='لست سکند').first()
        context['microsoft_products'] = Product.objects.filter(brand__url_title__iexact='microsoft').all()
        data = dict()
        categories = ProductCategory.objects.filter(is_active=True, Parent=None).all()[:3]
        for cat in categories:
            pro = list()
            for product in Product.objects.filter(is_active=True, category__url_title=cat.url_title).all()[:4]:
                pro.append(product)
            data[cat] = pro
        context['product_by_category'] = data

        return context


def header_components(request):
    return render(request, 'shared/header.html')


def footer_components(request):
    new_product = Product.objects.filter(is_new=True, is_active=True).all()[:3]
    inexpensive_product = Product.objects.filter(is_active=True).all().order_by('price')[:3]
    discount_product = Product.objects.filter(is_active=True, Discounted=True).all()[:3]
    all_categories = ProductCategory.objects.filter(Parent=None)[:7]
    all_brands = ProductBrand.objects.all()[:5]
    return render(request, 'shared/footer.html', context={
        'new_product': new_product,
        'inexpensive_product': inexpensive_product,
        'discount_product': discount_product,
        'all_categories': all_categories,
        'all_brands': all_brands,

    })


def about_us(request: HttpRequest):
    return render(request, 'home/about_us.html')


class ContactUs(View):
    def get(self, request):
        contact_form = ContactUsModelForm()
        return render(request, 'home/contactus.html', context={
            'form': contact_form
        })

    def post(self, request: HttpRequest):
        user_comment = ContactUsModelForm(request.POST)
        if user_comment.is_valid():
            user_comment.save()
            return redirect(reverse('index-page'))
        user_comment = ContactUsModelForm()
        return render(request, 'home/contactus.html', context={
            'form': user_comment
        })


def faq(request):
    return render(request, 'home/faq.html')
