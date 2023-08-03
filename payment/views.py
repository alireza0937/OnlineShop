from datetime import datetime
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import View

from order.models import Order, OrderDetail
from payment.forms import PaymentForm


def checkout(request: HttpRequest):
    return render(request, 'payment/cart.html')


def terms_and_conditions(request: HttpRequest):
    return render(request, 'payment/terms_and_conditions.html')


class CheckoutView(View):
    def get(self, request: HttpRequest):
        order = Order.objects.filter(is_paid=False, user_id=request.user.id).first()
        order_products = OrderDetail.objects.filter(orderby_id=order.id).all()
        payment_form = PaymentForm()
        return render(request, 'payment/cart.html', context={
            'all_orders': order_products,
            'total_price': order.calculate_basket_total_price(),
            'form': payment_form
        })

    def post(self, request: HttpRequest):
        payment_form = PaymentForm(request.POST)
        if payment_form.is_valid():
            user_order = Order.objects.filter(user_id=request.user.id, is_paid=False).first()
            user_order.total_price = user_order.calculate_basket_total_price()
            user_order.is_paid = True
            user_order.payment_date = datetime.today()
            user_order.save()
            return render(request, 'payment/payment_response.html')
        return HttpResponse("Wrong Information.")
