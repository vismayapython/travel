from django.db import models


# Create your models here.

class place(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pictures')
    des = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default=False)

class newspost(models.Model):
    name=models.CharField(max_length=100)
    img=models.ImageField(upload_to='pictures')
    month=models.CharField(max_length=50)
    date=models.CharField(max_length=50)
    des=models.TextField()

