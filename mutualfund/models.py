from django.db import models

# Create your models here.

class Mutualfunds(models.Model):
	company =models.CharField(max_length=50) 
	duration = models.IntegerField()
	returns = models.FloatField(null=True, blank=True, default=None)
	rank = models.IntegerField()
	