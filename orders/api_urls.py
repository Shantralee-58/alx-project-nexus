from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import OrderViewSet

# Create a router to handle the ViewSet URLs automatically
router = DefaultRouter()

# Register the OrderViewSet to handle /api/orders/
# This automatically creates two routes:
# 1. /api/orders/ (GET for list, POST for create)
# 2. /api/orders/{id}/ (GET/PUT/DELETE for specific order)
router.register(r'orders', OrderViewSet, basename='order')

urlpatterns = [
    # Include the router URLs
    path('', include(router.urls)),
]
