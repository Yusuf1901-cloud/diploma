from django.db import models
from django.utils import timezone
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Vehicle(models.Model):
    class VehicleTypes(models.TextChoices):
        SMALL = 'SML', 'SMALL'
        MIDDLE = 'MID', 'MIDDLE'
        BIG = 'BIG', 'BIG'
        SPB = 'SPB', 'SUPER BIG' 
    model_name = models.CharField(max_length=50, null=True, blank=True)
    car_num = models.CharField(max_length=8, unique=True)
    capacity = models.FloatField(default=3.5)
    state = models.BooleanField(default=True)
    type = models.CharField(max_length=3, choices=VehicleTypes.choices, default=VehicleTypes.MIDDLE)
    
    def __str__(self) -> str:
        return f"Vehicle with {self.car_num} number!"
    
class Location(models.Model):
    address = models.CharField(max_length=200, unique=True)
    lattitude = models.FloatField()
    longitude = models.FloatField()
    
    def __str__(self):
        return self.address
    
class PreOrderFromClient(models.Model):
    class Status(models.TextChoices):
        NEW = 'NW', 'New'
        BEING_REVIEWED = 'RW', 'Being Reviewed'
        ACCEPTED = 'AC', 'Accepted'
        DELIVERED = 'DV', 'Delivered'
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pre_orders') 
    from_adrs = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='from_adr_pre_rder')
    to_adrs = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='to_ad_pre_order')
    luggage_aprox = models.DecimalField(max_digits=5, decimal_places=2)
    price_invited_from_client = models.DecimalField(max_digits=13, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.NEW)
    
    class Meta:
        ordering = ['-created_at']
        
    def __str__(self) -> str:
        return f'{self.user.email} emailli clientdan buyurtma'
    
class Driver(models.Model):
    fio = models.CharField(max_length=100)
    phone_num = models.CharField(max_length=13, unique=True)
    tg_username = models.CharField(max_length=100, unique=True, null=True, blank=True)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name='drivers')

    def __str__(self) -> str:
        return f"{self.fio} ning obyekti"
    
class Order(models.Model):
    pre_order = models.ForeignKey(PreOrderFromClient, on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    couped_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-couped_at']
        indexes = [
            models.Index(fields=['-couped_at']),
        ]