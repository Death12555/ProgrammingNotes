from django.db import models
from datetime import datetime

# Create your models here.
class Features(models.Model):
    name = models.CharField(max_length=100, default= 'Attribute name')
    details = models.CharField(max_length=100, default= 'Checker value')

class Post(models.Model):
    title= models.CharField(max_length= 100)
    body= models.CharField(max_length= 1000000)
    creation_date= models.DateTimeField(default= datetime.now, blank=True)