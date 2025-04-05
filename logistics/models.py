from django.db import models
from orders.models import Order

class Warehouse(models.Model):
    location = models.CharField(max_length=255)
    capacity = models.PositiveIntegerField()

    def __str__(self):
        return self.location

class Shipment(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=20, choices=[('Pending', 'Pending'), ('Shipped', 'Shipped'), ('Delivered', 'Delivered')], default='Pending')
    tracking_number = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f"Shipment {self.id} - {self.status}"

class Fleet(models.Model):
    vehicle_number = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.vehicle_number

class Driver(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    vehicle = models.ForeignKey(Fleet, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
