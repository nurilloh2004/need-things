from django.urls import path
from .views import *


app_name = "myprint"

urlpatterns = [
    path('', homepage, name='home'),
    path('product/', product, name='product'),
    path('top_product/', top_product, name='top_product'),
    path('gift_product/', gift_productpage, name='gift_product'),
    path('order_view/', user_order_view, name='order_view')
    
]