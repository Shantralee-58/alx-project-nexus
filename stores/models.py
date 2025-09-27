from django.db import models

class Store(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255, default='N/A')
    city = models.CharField(max_length=100, default='Unknown City')
    zip_code = models.CharField(max_length=10, default='0000')

    def __str__(self):
        return self.name
    
    def full_address(self):
        return f"{self.address}, {self.city} {self.zip_code}"
