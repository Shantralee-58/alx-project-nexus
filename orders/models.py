from django.db import models
from django.conf import settings
from products.models import Product # Assuming Product model is here

class Order(models.Model):
    # Link the order to the User
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    # Order metadata
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, default='Pending')
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    # Shipping/Billing info (can be expanded later)
    shipping_address = models.TextField()

    def __str__(self):
        return f'Order {self.id} by {self.user.username}'

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2) # Price at time of order

    def __str__(self):
        return f'{self.quantity} of {self.product.name}'
