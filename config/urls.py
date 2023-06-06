from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('', include('account.urls')),
    path('', include('product.urls')),
    path('blogs/', include('article.urls')),
    path('dashboard/', include('userpanel.urls')),
    path('compare/', include('compare.urls')),
    path('wishlist/', include('wishlist.urls')),
    path('orders/', include('order.urls')),
    path('payment/', include('payment.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
