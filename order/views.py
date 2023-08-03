from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, JsonResponse
from django.shortcuts import render
from discount.models import DiscountCode
from order.models import Order, OrderDetail


@login_required
def user_cart(request: HttpRequest):
    empty = False
    coupon_code = request.GET.get('coupon')
    user_order = Order.objects.filter(is_paid=False, user_id=request.user.id).first()
    order_detail = OrderDetail.objects.filter(orderby_id=user_order.id).all().order_by('pk')
    if len(order_detail) == 0:
        empty = True
        return render(request, 'order/user_cart.html', context={
            'empty': empty
        })
    total_price = user_order.calculate_basket_total_price()
    if coupon_code is not None:
        code_validation = DiscountCode.objects.filter(code__iexact=coupon_code, is_active=True).first()
        if code_validation is not None:
            if code_validation.user is None:
                new_total_price = user_order.calculate_basket_total_price() - \
                                  (code_validation.discount_percentage * user_order.calculate_basket_total_price())

                code_validation.is_active = False
                code_validation.save()

                return render(request, 'order/user_cart.html', context={
                    'order_detail': order_detail,
                    'price': new_total_price,
                    'empty': empty,
                })
            else:
                if code_validation.user == request.user.id:
                    new_total_price = user_order.calculate_basket_total_price() - \
                                      (code_validation.discount_percentage * user_order.calculate_basket_total_price())
                    code_validation.is_active = False
                    code_validation.save()
                    return render(request, 'order/user_cart.html', context={
                        'order_detail': order_detail,
                        'price': new_total_price,
                        'empty': empty,
                    })

                else:
                    pass

        return render(request, 'order/user_cart.html', context={
            'message': True,
            'order_detail': order_detail,
            'price': total_price,
            'empty': empty,

        })

    return render(request, 'order/user_cart.html', context={
        'order_detail': order_detail,
        'price': total_price,
        'empty': empty,
    })


@login_required
def add_product_to_basket(request: HttpRequest):
    product_id = request.GET.get('id')
    product_count = request.GET.get('cnt')
    if int(product_count) < 1:
        product_count = 1
    user = request.user.id
    has_open_basket = Order.objects.filter(user_id=user, is_paid=False).first()
    if has_open_basket:
        already_in_order_basket = OrderDetail.objects.filter(product_id=product_id).first()
        if already_in_order_basket is not None:
            already_in_order_basket.count = product_count
            already_in_order_basket.save()
        else:
            OrderDetail.objects.filter(orderby_id=has_open_basket.id)
            new_product_add = OrderDetail(orderby_id=has_open_basket.id,
                                          product_id=product_id,
                                          count=product_count,
                                          )
            new_product_add.save()
            new_product_add.final_price = new_product_add.calculate_each_product_price()
            new_product_add.save()

        return JsonResponse({
            'status': 'successfully',
            'text': 'Successfully added to your basket',
            'icon': 'success'
        })
    else:
        new_order_basket = Order(user_id=user)
        new_order_basket.save()
        add_product = OrderDetail(orderby_id=new_order_basket.id,
                                  product_id=product_id,
                                  count=product_count,
                                  )
        add_product.save()
        add_product.final_price = add_product.calculate_each_product_price()
        add_product.save()

    return JsonResponse({
        'status': 'successfully',
        'text': 'Successfully added to your basket',
        'icon': 'success'
    })


@login_required
def change_count(request: HttpRequest):
    product_id = request.GET.get('id')
    operation = request.GET.get('operation')
    order_id = request.GET.get('order_id')
    product = OrderDetail.objects.filter(orderby_id=order_id, product_id=product_id).first()
    if operation == 'add':
        if product.count < 12:
            product.count += 1
    else:
        if product.count >= 2:
            product.count -= 1

    product.final_price = product.calculate_each_product_price()
    product.save()
    return render(request, 'order/user_cart.html')


def remove_product_from_order_list(request: HttpRequest):
    product_id = request.GET.get('id')
    order_id = request.GET.get('order_id')
    product = OrderDetail.objects.filter(product_id=product_id, orderby_id=order_id).first()
    product.delete()
    return render(request, 'order/user_cart.html')


def show_all_orders(request: HttpRequest):
    user = Order.objects.filter(is_paid=False, user_id=request.user.id).first()
    empty = False
    if user is not None:
        total_price = user.calculate_basket_total_price()
        user_orders = OrderDetail.objects.filter(orderby_id=user.id).all()

        return render(request, 'order/components/order_info.html', context={
            'all_product': user_orders,
            'total_price': total_price,
        })
    empty = True
    return render(request, 'order/components/order_info.html', context={
        'empty': empty
    })