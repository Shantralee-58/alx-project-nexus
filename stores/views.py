from django.shortcuts import render
from .models import Store

def store_list_view(request):
    """
    Displays a list of all sustainable stores from the database.
    """
    stores = Store.objects.all()
    context = {
        'stores': stores
    }
    return render(request, 'stores/store_list.html', context)
