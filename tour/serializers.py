from rest_framework import serializers
from tour.models import Tour, Image
from drf_extra_fields.fields import Base64ImageField
from django.utils.translation import ugettext_lazy as _

YOUR_MAX = 10
TEXT_MIN = 20
DEFAULT_MIN = 2
# images
class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'
# tour
class TourSerializer(serializers.ModelSerializer):
    # images = Base64ImageField(required=False)
    default_error_messages = {
        'error_length':_('The length must be greater than 10'),
        'error_content':_('Content Length mus be greater than 20.'),
        'error_price':_('Price must bo greater than 1')
    }
    class Meta:
        model = Tour
        fields = '__all__'

    def validate(self, attrs):
        if len(attrs['name']) < YOUR_MAX:
            raise serializers.ValidationError(self.error_messages['error_length'])
        return attrs