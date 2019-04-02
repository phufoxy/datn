from django.contrib import admin
from restaurants.models import Restaurant, RestaurantDetails

# Register your models here.
admin.site.register(Restaurant)
admin.site.register(RestaurantDetails)
