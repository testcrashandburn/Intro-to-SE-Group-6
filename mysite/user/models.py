from django.db import models

# Model for user Database
class User(models.Model):
    userID = models.BigAutoField(primary_key= True, unique= True)
    name = models.CharField(max_length = 90)
    email = models.EmailField(max_length = 200)
    password = models.CharField(max_length = 25, null = False)
    phone = models.PositiveBigIntegerField(blank = True)
    address = models.CharField(max_length = 300, blank = False)
    