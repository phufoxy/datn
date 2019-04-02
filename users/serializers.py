from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

from rest_framework import serializers
from rest_framework.authtoken.models import Token

# Register
class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)
    images = serializers.FileField(upload_to = 'tour/%Y/%m/%d/%H/%M/%S/',default='/default/default.png')
    class Meta:
        model = User
        # fields = ('id', 'username', 'email', 'password', 'confirm_password', 'date_jo"oined')
        fields = '__all__'

    def create(self, validated_data):
        user  = User.objects.create(
            username = validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
        # return super(UserRegistrationSerializer,self).create(validated_data)


    def validate(self, attrs):
        if attrs.get('password') != attrs.get('confirm_password'):
            raise serializers.ValidationError('Password does not match')
        return attrs

# LoginSerializer
class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)

    default_error_messages = {
        'error_account':_('User account is disable.'),
        'error_exists':_('User not exists to system.')
    }

    def __init__(self, *args, **kwargs):
        super(UserLoginSerializer, self).__init__(*args, **kwargs)
        self.user = None

    def validate(self, attrs):
        self.user = authenticate(username=attrs.get("username"), password=attrs.get('password'))
        if self.user:
            if not self.user.is_active:
                raise serializers.ValidationError(self.error_messages['error_account'])
            return attrs
        else:
            raise serializers.ValidationError(self.error_messages['error_exists'])


class TokenSerializer(serializers.ModelSerializer):
    auth_token = serializers.CharField(source='key')

    class Meta:
        model = Token
        fields = ("auth_token", "created")
    
