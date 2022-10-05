from django.urls import path
from .views import *

app_name = "accounts"


urlpatterns = [
    path('accounts/password_change/', password_new, name='password_newpage'),
    path('accounts/password_reset/', password_reset, name='password_reset'),
    path('accounts/register/', register, name='registerpage'),
    path('accounts/user_orderspage/', user_orders, name='user_order'),
    path('accounts/user_productspage/', user_products, name='user_product'),
    path('accounts/user_login_view/', login, name='login'),
    path('accounts/logout/', logout, name='user_logout')
]