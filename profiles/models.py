from django.db import models

# Create your models here.

class profiles(models.Model):
	username =models.CharField(max_length=50) 
	age = models.IntegerField()
	email =models.EmailField(max_length=100)
	profession =models.CharField(max_length=100)
	mobile = models.IntegerField()
	csaving = models.IntegerField()
	pmsaving = models.IntegerField()
	durinv = models.IntegerField()
	risk = models.IntegerField()
