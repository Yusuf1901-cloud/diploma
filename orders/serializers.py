from rest_framework import serializers
from . import models


class LocationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.Location
        fields = ['id', 'address', 'lattitude', 'longitude']
    
        
class PreOderSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PreOrderFromClient
        fields = ['id', 'user', 'created_at',
                  'from_adrs', 'to_adrs',
                  'luggage_aprox', 'status',
                  'price_invited_from_client']
        
class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Driver
        fields = ['id', 'fio', 'phone_num', 'tg_username', 'vehicle']
        
        
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Order
        fields = ['id', 'pre_order', 'driver', 'couped_at']