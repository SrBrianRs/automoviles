from django.db import models
from django.conf import settings
# Create your models here.

class Consulta(models.Model):
    fecha = models.TextField(default='',blank=False)
    modelo = models.TextField(default='',blank=False)
    prompt = models.TextField(default='',blank=False)
    result = models.TextField(default='',blank=False)
    posted_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)