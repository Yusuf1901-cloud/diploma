from rest_framework import generics
from rest_framework import permissions, authentication

from . import models
from . import serializers

class LocationListCreateAPIView(generics.ListCreateAPIView):
    queryset = models.Location.objects.all()
    serializer_class = serializers.LocationSerializer
    authentication_classes = [authentication.BasicAuthentication]


class LocationDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Location.objects.all()
    serializer_class = serializers.LocationSerializer
    permission_classes = [permissions.IsAdminUser,]
    authentication_classes = [authentication.BasicAuthentication]


class PreOrderAPIView(generics.ListCreateAPIView):
    queryset = models.PreOrderFromClient.objects.all()
    serializer_class = serializers.PreOderSerializer
    permission_classes = [permissions.IsAuthenticated]

class DriverListCreateAPIView(generics.ListCreateAPIView):
    queryset = models.Driver.objects.all()
    serializer_class = serializers.DriverSerializer
    permission_classes = [permissions.IsAdminUser]
    
    
class DriverDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Driver.objects.all()
    serializer_class = serializers.DriverSerializer
    permission_classes = [permissions.IsAdminUser]

    
class OrderListCreateAPIVIew(generics.ListCreateAPIView):
    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderSerializer
    permission_classes = [permissions.IsAdminUser]
    