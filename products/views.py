from django.shortcuts import render
from .models import Product 

def product_list_view(request):
    # Fetch ALL products from the PostgreSQL database
    products_queryset = Product.objects.all().order_by('name') 

    context = {
        'products': products_queryset,
        # Static data for sidebar filters (for template rendering)
        'categories': ['Eco Services', 'Eco Gadgets', 'Sustainable Clothing', 'Organic Food', 'Reusable Items'],
        'eco_labels': ['Organic', 'Recycled', 'Vegan', 'Fair Trade']
    }
    
    return render(request, 'products/product_list.html', context)
