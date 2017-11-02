from django.db import models

# Create your models here.

class fd(models.Model):
	id1 =models.IntegerField() 
	bank = models.CharField(max_length=20)
	min_duration = models.IntegerField()
	max_duration = models.IntegerField()
	interest = models.FloatField(null=True, blank=True, default=None)
	amount_upto = models.IntegerField() 
