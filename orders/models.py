from django.db import models
from django.contrib.auth import get_user_model
import uuid

User = get_user_model()

class Order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    store = models.ForeignKey('products.Store', on_delete=models.CASCADE)  # string reference
    total_cents = models.IntegerField()
    status = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

class OrderItem(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE)  # string reference
    price_cents = models.IntegerField()
    quantity = models.IntegerField()

