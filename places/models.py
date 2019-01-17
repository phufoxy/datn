from django.db import models
from datetime import datetime    
from django.utils import timezone

# Create your models here.
class TypeInfo(models.Model):
    city = models.CharField(max_length=250,default='Đà Nẵng')
    address = models.CharField(max_length=250,null=True,blank=True)
    type = models.CharField(max_length=250,default='Núi')

    class Meta:
        abstract = True
        ordering = ["-id"]
    
class Place(TypeInfo):
    name = models.CharField(max_length=250)
    images = models.FileField(upload_to = 'place/%Y/%m/%d',default='/default/images.jpg')
    review = models.IntegerField(default=0)
    price = models.FloatField(default=0,null=True,blank=True)
    content = models.TextField(default="Null")
    date_create = models.DateTimeField(default=timezone.now(), blank=True)

    def __str__(self):
        return self.name + '-' + self.city