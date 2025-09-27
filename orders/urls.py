from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    # Maps /orders/ to the order_list_view
    path('', views.order_list_view, name='order_list'),
]
