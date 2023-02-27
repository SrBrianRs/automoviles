from django.db import models

# Create your models here.

class Car(models.Model):
    brand = models.TextField(default='',blank=False)
    model = models.TextField(default='',blank=False)
    color = models.TextField(default='',blank=False)
    version = models.TextField(default='',blank=False)
    year = models.IntegerField()
    engine = models.TextField(default='',blank=False)
    consumption = models.DecimalField(max_digits=4, decimal_places=2)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    airbags = models.BooleanField()
    absbreak = models.BooleanField()
