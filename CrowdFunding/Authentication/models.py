from django.db import models

# Create your models here.
class Users(models.Model):
    user_id=models.AutoField(primary_key=True)
    First_name=models.CharField(max_length=100)
    Last_name=models.CharField(max_length=100)
    password=models.BigIntegerField()
    image = models.ImageField()
    email = models.EmailField(max_length=254)
    active=models.BooleanField()
    phone=models.BigIntegerField()
    def __str__(self):
        return self.First_name
