from django.db import models
from product.models import Product
from user.models import User
# Create your models here.
class Transaction(models.Model):
    transactionID = models.AutoField(primary_key= True, unique= True)
    #productInfo = models.ForeignKey(Product, on_delete = models.CASCADE)
    #userInfo = models.ForeignKey(User, on_delete = models.CASCADE)
    #sellerID = models.ForeignKey(User, on_delete = models.CASCADE)
    transactionTime = models.DateTimeField(auto_now = True)
    #price = models.ForeignKey(Product, to_field = Product._productID, on_delete = models.CASCADE)
    