from django.contrib.auth import get_user_model
from phonenumber_field.formfields import PhoneNumberField
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import PhoneToken

User = get_user_model()


class PhoneTokenCreateSerializer(ModelSerializer):
    phone_number = serializers.CharField(validators=PhoneNumberField().validators)

    class Meta:
        model = PhoneToken
        fields = ('reference_id', 'phone_number')


class PhoneTokenUser(ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'


class PhoneTokenValidateSerializer(ModelSerializer):
    otp = serializers.CharField(max_length=40)
    reference_id = serializers.CharField(max_length=12)

    class Meta:
        model = PhoneToken
        fields = ('reference_id', 'otp')
