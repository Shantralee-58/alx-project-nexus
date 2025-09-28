from rest_framework import serializers
from .models import Category, Product

class CategorySerializer(serializers.ModelSerializer):
    """
    Serializer for the Category model.
    """
    class Meta:
        model = Category
        fields = ('id', 'name', 'slug', 'description')
        read_only_fields = ('slug',)

class ProductSerializer(serializers.ModelSerializer):
    """
    Serializer for the Product model.
    It includes the Category name as a read-only field for easy viewing.
    """
    category_name = serializers.CharField(source='category.name', read_only=True)

    class Meta:
        model = Product
        # Include all relevant fields, plus the read-only category name
        fields = ('id', 'category', 'category_name', 'name', 'slug', 'description', 
                  'price', 'is_available', 'stock', 'image', 
                  'created_at', 'updated_at')
        read_only_fields = ('slug',)
