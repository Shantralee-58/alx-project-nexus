from rest_framework.routers import DefaultRouter
from .api_views import CategoryViewSet, ProductViewSet

# Create a router instance
router = DefaultRouter()

# Register the viewsets to create the URL patterns
# This automatically generates: /categories/, /categories/{id}/, /products/, /products/{id}/
router.register(r'categories', CategoryViewSet)
router.register(r'products', ProductViewSet)

# The urlpatterns will contain all the generated URLs
urlpatterns = router.urls
