from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(default="No description")

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(default="No description")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        default=1  # temporary default id
    )

    def __str__(self):
        return self.name

