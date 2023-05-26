from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView
from home.forms import ContactUsModelForm
from product.models import ProductVisit, Product
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
        return context


def header_components(request):
    return render(request, 'shared/header.html')


def footer_components(request):
    return render(request, 'shared/footer.html')


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
