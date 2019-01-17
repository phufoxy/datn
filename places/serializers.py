from rest_framework import serializers
from places.models import Place
from drf_extra_fields.fields import Base64ImageField
from django.utils.translation import ugettext_lazy as _

YOUR_MAX = 10
TEXT_MIN = 20
# Place 
class PlaceSerializer(serializers.ModelSerializer):
    images = Base64ImageField(required=False)
    default_error_messages = {
        'error_length':_('The length must be greater than 10'),
        'error_content':_('Content Length mus be greater than 20.'),
        'error_price':_('Price must bo greater than 1')
    }
    class Meta:
        model = Place
        fields = '__all__'

    def validate(self, attrs):
        if len(attrs['name']) < YOUR_MAX:
            raise serializers.ValidationError(self.error_messages['error_length'])
        if len(attrs['content']) < TEXT_MIN:
            raise serializers.ValidationError(self.error_messages['error_content'])

        return attrs