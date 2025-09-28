from rest_framework import viewsets
from rest_framework.filters import OrderingFilter 
import django_filters # <-- IMPORTANT
from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer
from .filters import ProductFilter  
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser

class IsAdminUserOrReadOnly(IsAdminUser):
    """
    Custom permission where only Django Admin users can perform PUT, POST, DELETE.
    Everyone (authenticated or not) can perform GET (read).
    """
    def has_permission(self, request, view):
        # Allow GET, HEAD, OPTIONS requests (safe methods) for all users
        is_safe_method = request.method in ('GET', 'HEAD', 'OPTIONS')

        # If it's a safe method, grant permission (read-only)
        if is_safe_method:
            return True

        # Otherwise (for PUT, POST, DELETE), check if the user is an admin
        return super().has_permission(request, view)

class CategoryViewSet(viewsets.ModelViewSet):
    """
    Provides CRUD operations for Category.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    # permission_classes = [IsAdminUserOrReadOnly] 

class ProductViewSet(viewsets.ModelViewSet):
    """
    Provides CRUD operations for Product, with added filtering, sorting, and pagination.
    """
    queryset = Product.objects.select_related('category').all()
    serializer_class = ProductSerializer
    
    # Removed 'filters.' and used the directly imported 'OrderingFilter'
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend, OrderingFilter)
    filterset_class = ProductFilter 
    
    ordering_fields = ['price', 'name', 'created_at']
    ordering = ['name'] # Default ordering

    # permission_classes = [IsAdminUserOrReadOnly] 
