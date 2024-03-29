from django.db import models
from accounts.models import CustomUser

# Product Database Model
class Product(models.Model):
    print('model for product class')
    _productID = models.AutoField(primary_key = True)
    _productName = models.CharField(max_length = 200)
    _productDescript = models.TextField()
    price = models.DecimalField(max_digits = 12, decimal_places = 2)
    quantity = models.IntegerField()
    seller = models.ForeignKey(CustomUser, on_delete = models.CASCADE)

    class Meta:
        ordering = ['_productName']

    def __str__(self):
        return self._productName
