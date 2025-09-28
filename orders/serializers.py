from rest_framework import serializers
from .models import Order, OrderItem
from products.models import Product

# ----------------- 1. Nested Serializer for Order Items -----------------
# ... (OrderItemSerializer remains the same) ...

class OrderItemSerializer(serializers.ModelSerializer):
    """
    Serializer used for displaying order items within a fetched Order.
    Shows the product name, price at time of order, and quantity.
    """
    product_name = serializers.ReadOnlyField(source='product.name')

    class Meta:
        model = OrderItem
        fields = ['product', 'product_name', 'price', 'quantity']
        read_only_fields = ['price'] # Price is set automatically during creation, not user input


# ----------------- 2. Serializer for Creating/Placing a New Order -----------------

class OrderCreateItemSerializer(serializers.Serializer):
# ... (OrderCreateItemSerializer remains the same) ...
    """
    Serializer used ONLY for receiving data when a user places a new order (POST).
    It expects product ID and quantity from the front-end cart.
    """
    product_id = serializers.IntegerField()
    quantity = serializers.IntegerField()

    def validate_product_id(self, value):
        """Check if the product exists and is available."""
# ... (validate_product_id remains the same) ...
        try:
            product = Product.objects.get(id=value, is_available=True)
        except Product.DoesNotExist:
            raise serializers.ValidationError(f"Product with ID {value} does not exist or is unavailable.")
        self.context['product'] = product
        return value

    def validate(self, data):
# ... (validate remains the same) ...
        """Check if requested quantity is available in stock."""
        product = self.context.get('product')
        quantity = data.get('quantity')

        if quantity <= 0:
             raise serializers.ValidationError("Quantity must be a positive number.")

        if product and quantity > product.stock:
            raise serializers.ValidationError(f"Only {product.stock} units of {product.name} are available in stock.")
        
        # --- FIX START ---
        # Add the product instance to the validated data for the item.
        # This makes it available in validated_data['items'] for the parent serializer's create method.
        data['product'] = product
        # --- FIX END ---
        
        return data


class OrderCreateSerializer(serializers.ModelSerializer):
    """
    Serializer used for receiving order details (shipping info) and validating order items.
    """
    # This field receives the list of items from the front-end
    items = OrderCreateItemSerializer(many=True, write_only=True)
    
    # Read-only display of the final items and total cost
    order_items = OrderItemSerializer(many=True, read_only=True, source='items')
    total_cost = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True, source='get_total_cost')
    
    class Meta:
        model = Order
        # Fields user inputs (shipping info) + the order items list (items)
        fields = [
            'id', 'first_name', 'last_name', 'email', 'address', 
            'postal_code', 'city', 'items', 'created_at', 
            'order_items', 'total_cost', 'status'
        ]
        # Ensure 'user' is read-only, not expecting user input
        read_only_fields = ['user', 'paid', 'status', 'created_at', 'updated_at']

    def create(self, validated_data):
        """
        Custom create method to handle order and order item creation in one transaction,
        and update the product stock.
        """
        # 1. Extract the validated items list
        items_data = validated_data.pop('items')
        
        # 2. Get the requesting user from the view context
        user = self.context['request'].user
        
        # 3. CRUCIAL FIX: Ensure 'user' is not already in validated_data before passing it.
        validated_data.pop('user', None)

        # 4. Create the main Order instance
        order = Order.objects.create(user=user, **validated_data)

        # 5. Create OrderItem instances and update stock
        for item_data in items_data:
            # FIX: 'product' is now safely available in item_data thanks to the validate() method above.
            product = item_data['product'] 
            quantity = item_data['quantity']
            
            # Create the OrderItem
            OrderItem.objects.create(
                order=order,
                product=product,
                price=product.price, # Record the current price
                quantity=quantity
            )
            
            # Decrease product stock
            product.stock -= quantity
            product.save()

        return order

