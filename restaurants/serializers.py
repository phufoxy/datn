from rest_framework import serializers
from restaurants.models import Restaurant, RestaurantDetails
from drf_extra_fields.fields import Base64ImageField
from django.utils.translation import ugettext_lazy as _

YOUR_MAX = 10
TEXT_MIN = 20
DEFAULT_MIN = 2
# restaurants details
# Serializer
class RestaurantdetailSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = RestaurantDetails
        fields = '__all__'
# restaurants
# Place 
class RestaurantSerializer(serializers.ModelSerializer):
    details = RestaurantdetailSerializer(many=True, read_only=True)
    # images = Base64ImageField(required=False)
    default_error_messages = {
        'error_length':_('The length must be greater than 10'),
        'error_content':_('Content Length mus be greater than 20.'),
        'error_price':_('Price must bo greater than 1')
    }
    class Meta:
        model = Restaurant
        fields = '__all__'

    def validate(self, attrs):
        if len(attrs['name']) < YOUR_MAX:
            raise serializers.ValidationError(self.error_messages['error_length'])
        if len(attrs['content']) < TEXT_MIN:
            raise serializers.ValidationError(self.error_messages['error_content'])
        return attrs