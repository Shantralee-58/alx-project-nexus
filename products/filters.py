import django_filters
from .models import Product

class ProductFilter(django_filters.FilterSet):
    """
    Defines filters for the Product model based on the project goals.
    Allows filtering by:
    - category (exact match of category ID)
    - price (range: price_min and price_max)
    """
    
    # 1. Filter by price range
    price_min = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    price_max = django_filters.NumberFilter(field_name='price', lookup_expr='lte')

    class Meta:
        model = Product
        fields = {
            # 2. Filter by category ID (allows /products/?category=1)
            'category': ['exact'],
            # 3. Filter by availability
            'is_available': ['exact'],
        }
