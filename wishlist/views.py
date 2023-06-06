from django.http import HttpRequest, JsonResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from product.models import Product
from wishlist.models import WishList, WishlistDetails


@login_required
def add_wishlist(request: HttpRequest):
    user = request.user.id
    product_id = request.GET.get('id')
    product_slug = request.GET.get('slug')
    has_wishlist = WishList.objects.filter(user_id=user).first()
    product_info = Product.objects.filter(slug__iexact=product_slug).first()
    if has_wishlist:
        if not WishlistDetails.objects.filter(product_id=product_id).first():
            new_product_add_to_wishlist = WishlistDetails(order_id=has_wishlist.id,
                                                          product_id=product_id,
                                                          price=product_info.price)
            new_product_add_to_wishlist.save()
        else:
            return JsonResponse({
                'status': 'unsuccessfully',
                'icon': 'unsuccess',
                'text': "This Product Already Been In Your WishList!",
                'confirmButtonText': 'OK'
            })
    else:
        new_wishlist = WishList(user_id=user)
        new_wishlist.save()
        wishlist_details = WishlistDetails(order_id=new_wishlist.id,
                                           product_id=product_id,
                                           price=product_info.price)

        wishlist_details.save()
    return JsonResponse({
        'status': 'successfully',
        'icon': 'success',
        'text': "This Product Add To Your WishList!",
        'confirmButtonText': 'OK'
    })

@login_required
def show_wishlist(request: HttpRequest):
    user_wishlist = WishlistDetails.objects.filter(order__user=request.user.id).all()
    return render(request, 'wishlist/wishlist.html', context={
        'user_wishlist': user_wishlist
    })
