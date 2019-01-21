from django.db import models
from places.models import TypeInfo
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class House(TypeInfo):
    name = models.CharField(max_length=250)
    images = models.FileField(upload_to = 'house/%Y/%m/%d/%H/%M/%S/',default='/default/default.png')
    review = models.IntegerField(default=0)
    price = models.FloatField(default=0,null=True,blank=True)
    content = models.TextField(default="Null")
    date_create = models.DateTimeField(default=timezone.now, blank=True)

    def __str__(self):
        return self.name + '-' + self.city

class HouseDetails(models.Model):
    house = models.ForeignKey(House,related_name='details',on_delete=models.CASCADE)
    title = models.CharField(max_length=250,default="Null")
    body = RichTextUploadingField(default="Null")

    def __str__(self):
        return self.house.name
    
    class Meta:
        ordering = ["-id"]