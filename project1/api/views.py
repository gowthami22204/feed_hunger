from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from .serializers import LoginSerializer, SignUpSerializer
from .models import VolunteerUser
from django.contrib.auth import login
from rest_framework import status
from rest_framework.generics import GenericAPIView
# from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from django.conf import settings
from django.core.mail import send_mail
import random
import string
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from django.db.models import Q

def passcode():
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for i in range(6))
    print("Random password is:", password)
    return password

class SignUpView(generics.CreateAPIView):
    queryset = VolunteerUser.objects.all()
    serializer_class = SignUpSerializer
    
    def post(self, request):
        print(request.data, 'inside post')
        
        data = request.data.copy()
        otp = passcode()
        data['passcode'] = otp
        
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()  # Add this line to save the record
    
        # smtp passcode
        subject = 'Passcode Verification code'
        message = f'Hi, your passcode: {otp}. Thanks for registering with Helping Hands...'
        sender = settings.EMAIL_HOST_USER
        send_mail(subject, message, sender, [data['email']])
        
        return Response({'success': True}, status=status.HTTP_200_OK)




class LoginView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = LoginSerializer

    def post(self, request):
        print(request.data)
        volunteername = request.data.get('volunteername')
        passcode = request.data.get('passcode')
        print('data:',volunteername,passcode)
        if not volunteername or not passcode:
            return Response({'error': 'Please provide both email and passcode'}, status=status.HTTP_400_BAD_REQUEST)

        user = VolunteerUser.objects.get(volunteername=volunteername, passcode=passcode)

        if not user:
            return Response({'error': 'Invalid email or passcode'}, status)
        else:
            return Response({"success":'login successful...'})