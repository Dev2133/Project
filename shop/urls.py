
from django.urls import path
from shop.views import *

urlpatterns = [
    path('catalog/', catalog, name='catalog'),
    path('create_order/', create_order, name='create_order'),
    path('orders/', orders, name='orders'),
    path('product_detail/<int:product_id>/', product_detail, name='product_detail'),
]
