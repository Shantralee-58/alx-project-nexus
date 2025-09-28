from django.db import models
from django.conf import settings # Standard way to reference the User model
from products.models import Product # To link order items to the products they are buying

class Order(models.Model):
    """
    Represents a customer's order.
    """
    # Links the order to the User who placed it. CASCADE means if user is deleted, orders are too.
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='orders', on_delete=models.CASCADE)
    
    # Customer/Shipping Information (assuming a simple model here)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=250)
    postal_code = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    
    # Order Status and Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)
    
    # Simple Status field (you might use choices or an Enum in a more complex setup)
    ORDER_STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('processing', 'Processing'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled'),
    )
    status = models.CharField(max_length=20, choices=ORDER_STATUS_CHOICES, default='pending')

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return f'Order {self.id}'

    # Custom method to calculate the total cost of all items in the order
    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    """
    Represents a single item purchased within an order (e.g., 2 shirts).
    """
    # Link to the main Order (related_name='items' is used in Order.get_total_cost())
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    
    # Link to the Product from the catalog
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    
    # Snapshot of the price at the time of purchase (crucial if product price changes later)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)

    def get_cost(self):
        # Calculate the total cost for this single item type
        return self.price * self.quantity
