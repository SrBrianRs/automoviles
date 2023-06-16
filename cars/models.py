from django.db import models
from django.conf import settings
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
    posted_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)


class Vote(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    car = models.ForeignKey('cars.Car', related_name='cars', on_delete=models.CASCADE)