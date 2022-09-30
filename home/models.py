from django.db import models
import re


class Jewelry(models.Model):
    i = 10000
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=i, blank=False)
    type = models.CharField(max_length=i, blank=False)
    quantity = models.IntegerField(null=False)
    price = models.CharField(max_length=i, blank=False)
    price_int = models.IntegerField(null=True, blank=True)
    description = models.CharField(max_length=i, blank=False, default='Joya de plata 925.')
    size = models.IntegerField(null=True, blank=True)
    sold = models.BooleanField(null=False, default=False)
    picture = models.FileField(null=True)
