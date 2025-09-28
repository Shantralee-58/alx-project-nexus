from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Order

@login_required
def order_list_view(request):
    """
    Displays a list of all orders placed by the currently authenticated user.
    """
    # Filter orders by the current user and order them by the creation date (newest first).
    # NOTE: The field name must be 'created_at', not 'order_date'.
    orders = Order.objects.filter(user=request.user).order_by('-created_at')

    context = {
        'orders': orders
    }
    
    return render(request, 'orders/order_list.html', context)

