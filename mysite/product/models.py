from django.db import models
import random

# Create your models here.
class Product(models.Model):
    print('model for product class')
    _productID = models.AutoField(primary_key = True)
    _productName = models.CharField(max_length = 200)
    _productDescript = models.CharField(max_length = 750)
    price = models.DecimalField(max_digits = 12, decimal_places = 2)
    quantity = models.IntegerField()


