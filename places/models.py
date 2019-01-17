from django.db import models

# Create your models here.
class TypeInfo(models.Model):
    city = models.CharField(max_length=250,default='Đà Nẵng')
    address = models.CharField(max_length=250,null=True,blank=True)
    type = models.CharField(max_length=250,default='Núi')

    class Meta:
        abstract = True
    
class Place(TypeInfo):
    name = models.CharField(max_length=250)
    images = models.FileField(upload_to = 'place/',default='/default/images.jpg')
    review = models.IntegerField(default=0)
    price = models.FloatField(default=0,null=True,blank=True)
    content = models.TextField()

    def get_absolute_url(self):
        return reverse('ListPlace')

    def __str__(self):
        return self.name + '-' + self.city