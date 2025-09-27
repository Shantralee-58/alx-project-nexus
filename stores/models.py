from django.db import models

class Store(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=10)

    def __str__(self):
        return self.name

    class Meta:
        # Orders stores alphabetically by name
        ordering = ['name']
