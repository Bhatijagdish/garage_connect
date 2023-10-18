from datetime import date

from django.db import models
from django.utils import timezone

# Create your models here.
class FormData(models.Model):
    kenteken = models.CharField(max_length=50)
    kmstand = models.CharField(max_length=50)
    postcode = models.CharField(max_length=10)
    huisnummer = models.CharField(max_length=10)
    straatnaam = models.CharField(max_length=150)
    woonplaats = models.CharField(max_length=150)
    emailaddress = models.EmailField()

    onderhoud = models.CharField(max_length=400)
    werkzaamheden = models.JSONField(null=True, blank=True)
    datum = models.DateField()
    opmerkingen = models.TextField(null=True, blank=True)

