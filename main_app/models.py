from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Item(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    url = models.CharField(max_length=1000)
    max_price = models.IntegerField()
    status = models.BooleanField(default = False)
