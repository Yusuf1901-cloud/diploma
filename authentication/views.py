from django.shortcuts import render
from rest_framework import permissions
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_200_OK, HTTP_401_UNAUTHORIZED
from authentication.serializers import RegistrationSerializer, LoginSerializer
from django.contrib.auth import authenticate
from rest_framework import permissions, authentication

from authentication.models import CustomUser


class AuthUserAPIView(GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        user = request.user
        
        serializer = RegistrationSerializer(user)
        return Response({'user': serializer.data})
        
class RegisterAPIView(GenericAPIView):
    serializer_class = RegistrationSerializer
    permission_classes = [permissions.AllowAny,]
    authentication_classes = [authentication.BasicAuthentication,]
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    
class LoginAPIView(GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = [permissions.AllowAny,]
    authentication_classes = [authentication.BasicAuthentication,]

    def post(self, request):
        email = request.data.get('email', None)
        password = request.data.get('password',None)
        
        user = authenticate(username=email, password=password)
        
        if user:
            serializer = self.serializer_class(user)
            
            return Response(serializer.data, HTTP_200_OK)
        return Response({'message': "INvalid credentials try again"}, status=HTTP_401_UNAUTHORIZED)