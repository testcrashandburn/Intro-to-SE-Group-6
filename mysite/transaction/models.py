from django.db import models

# Create your models here.
from django.db import models
from product.models import Product
from accounts.models import CustomUser
# Create your models here.
class Transaction(models.Model):
    transactionID = models.AutoField(primary_key= True, unique= True)
    productInfo = models.ForeignKey(Product, on_delete = models.CASCADE)
    sellerInfo = models.ForeignKey(CustomUser, on_delete = models.CASCADE,)
    transactionTime = models.DateTimeField()
    tex=str(transactionTime)
    #price = models.ForeignKey(Product, to_field = Product._productID, on_delete = models.CASCADE)
    
    
   # print(tex)
    def __int__(self):
        return self.transactionTime