from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Order
from .serializers import OrderCreateSerializer, OrderItemSerializer

class OrderViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows authenticated users to view their own orders
    or place new orders.
    """
    # Only authenticated users can interact with this API
    permission_classes = [IsAuthenticated]
    
    # We use OrderCreateSerializer for both reading (displaying order items) and 
    # writing (receiving new orders).
    serializer_class = OrderCreateSerializer
    
    def get_queryset(self):
        """
        Custom queryset: ensures a user can only see the orders they placed.
        It also pre-fetches related items to reduce database queries.
        """
        # The request.user object is available because IsAuthenticated permission passed
        user = self.request.user
        
        # Filter orders by the current logged-in user and prefetch related order items
        return Order.objects.filter(user=user).prefetch_related('items__product')

    def perform_create(self, serializer):
        """
        Handles the POST request (order placement).
        Sets the 'user' field on the Order instance to the current logged-in user.
        """
        # The OrderCreateSerializer handles the stock update logic in its .create() method.
        # We pass the current user from the request context.
        serializer.save(user=self.request.user)

    def get_serializer_class(self):
        """
        If we needed a separate serializer for listing/retrieving vs creating, 
        we would use this method, but OrderCreateSerializer handles both needs well.
        For simplicity, we use the same serializer class set above.
        """
        return self.serializer_class

