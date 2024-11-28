# Order Model
from django.db import models

class Courier(models.Model):
    name = models.CharField(max_length=30)

class Order(models.Model):
    STATUS_OPTIONS = [
        ('assigned', 'Assigned'),
        ('accepted', 'Accepted'),
        ('declined', 'Declined'),
        ('picked_up', 'Picked Up'),
        ('in_transit', 'In Transit'),
        ('delivered', 'Delivered'),
    ]

    order_status = models.CharField(max_length=20, choices=STATUS_OPTIONS, default='assigned')
    courier = models.ForeignKey(Courier, on_delete=models.CASCADE)
    pickup_location = models.CharField(max_length=50)
    delivery_location = models.CharField(max_length=50)









































