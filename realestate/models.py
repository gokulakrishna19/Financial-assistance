from django.db import models

# Create your models here.

class Realestate(models.Model):
	area =models.CharField(max_length=50) 
	city = models.CharField(max_length=40)
	min_price = models.IntegerField()
	max_price = models.IntegerField()
	avg_price = models.IntegerField()
	avg_growth = models.FloatField(null=True, blank=True, default=None)
	
	types = models.CharField(max_length=50) 

