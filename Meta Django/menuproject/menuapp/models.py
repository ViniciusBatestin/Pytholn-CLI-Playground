from django.db import models
from unicodedata import name

# Create your models here.
class Menuitems(models.Model):
    itemname = models.CharField(max_length = 200)
    category = models.CharField(max_length = 300)
    year = models.IntegerField()
