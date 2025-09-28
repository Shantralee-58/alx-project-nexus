"""
URL configuration for sustainify project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# Import the JWT views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
    # ------------------ Django Admin & Auth ------------------
    path('admin/', admin.site.urls),
    # Built-in Django auth URLs (for login/logout/password reset if needed)
    path('accounts/', include(('django.contrib.auth.urls', 'accounts'), namespace='accounts')),
    path('', include('django.contrib.auth.urls')),

    # ------------------ Web Application Routes ------------------
    path('', include('home.urls')),
    path('products/', include('products.urls')),
    # Placeholder for web app orders pages (e.g., /orders/history)
    path('orders/', include('orders.urls')), 
    path('about/', include('about.urls')),
    path('stores/', include('stores.urls')),
    
    # ------------------ REST API Routes ------------------
    
    # 1. JWT Authentication Endpoints
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    
    # 2. E-Commerce Catalog API Routes (Products and Categories)
    path('api/catalog/', include('products.api_urls')),
    
    # 3. Order Management API Route (using /api/orders/)
    path('api/', include('orders.api_urls')), 
]

# Serve media files (like product images) in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

