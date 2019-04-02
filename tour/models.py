from django.db import models
from django.utils import timezone

# Create your models here.
class Tour(models.Model):
    name = models.CharField(max_length=250)
    images = models.FileField(upload_to = 'tour/%Y/%m/%d/%H/%M/%S/',default='/default/default.png')
    price = models.FloatField(default=0,null=True,blank=True)
    total = models.IntegerField(default="Null")
    date = models.FloatField(default=0,null=True,blank=True)
    date_create = models.DateTimeField(default=timezone.now, blank=True)

    def __str__(self):
        return self.name
# Upload Image
class Image(models.Model):
    name = models.CharField(max_length=250,default="Image Editor")
    images = models.FileField(upload_to = 'editor/%Y/%m/%d/%H/%M/%S/',default='/default/default.png')