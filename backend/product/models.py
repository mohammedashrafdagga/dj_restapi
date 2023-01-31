from django.db import models

# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=125)
    content = models.TextField(blank=True)
    price = models.DecimalField(max_digits=4, decimal_places=2, default=99.99)
