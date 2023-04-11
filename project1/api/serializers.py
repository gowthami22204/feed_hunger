from django.contrib.auth import get_user_model, authenticate
from rest_framework import serializers
from .models import VolunteerUser


# User = get_user_model()

class SignUpSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = VolunteerUser
        fields = [ 'first_name', 'last_name','volunteername','email', 'city','state','passcode','Areaofinterest']

    def create(self, validated_data):
        user = VolunteerUser.objects.create(
            email=validated_data['email'],
            state=validated_data['state'],
            city=validated_data['city'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            Areaofinterest=validated_data['Areaofinterest'],
            volunteername=validated_data['volunteername'],
            passcode=validated_data['passcode'],

        )
        return user
    
    #login

    
class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = VolunteerUser
        fields = ['volunteername', 'passcode']