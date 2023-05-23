from rest_framework import serializers
from .models import SiteUser


class UserRegistrationSerializer(serializers.ModelSerializer):

    class Meta:
        model = SiteUser
        fields = ('email', 'user_name', 'password', 'phone_number')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if(password is not None):
            instance.set_password(password)
        instance.save()
        return instance
