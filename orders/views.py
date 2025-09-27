from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Order

# Ensure the user is logged in to see their orders
@login_required 
def order_list_view(request):
    # Fetch orders belonging only to the current logged-in user
    user_orders = Order.objects.filter(user=request.user).order_by('-order_date')
    
    context = {
        'orders': user_orders
    }
    return render(request, 'orders/order_list.html', context)
