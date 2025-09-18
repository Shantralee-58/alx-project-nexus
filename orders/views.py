from django.shortcuts import render
from .models import Order

def order_list(request):
    orders = Order.objects.all().order_by('-created_at')  # latest first
    return render(request, 'orders/order_list.html', {'orders': orders})

