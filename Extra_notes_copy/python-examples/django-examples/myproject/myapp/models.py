from django.db import models

# Create your models here.
class Features(models.Model):
    name = models.CharField(max_length=100, default= 'Attribute name')
    details = models.CharField(max_length=100, default= 'Checker value')