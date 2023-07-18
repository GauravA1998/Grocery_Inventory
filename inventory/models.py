from django.db import models
from decimal import Decimal

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, default=None)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, default=None)


    def save(self, *args, **kwargs):
        self.discount = self.price * Decimal(0.2)
        self.total_amount = self.price - self.discount
        super(Product, self).save(*args, **kwargs)


    def __str__(self):
        return self.name

