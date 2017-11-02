from django.db import models

# Create your models here.

class insurance(models.Model):
	id1 =models.IntegerField() 

	company = models.CharField(max_length=20)
	types = models.CharField(max_length=100)
	duration = models.IntegerField()
	
	ytd = models.FloatField(null=True, blank=True, default=None)
	interest = models.FloatField(null=True, blank=True, default=None)
	 
