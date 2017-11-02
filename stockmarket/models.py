from django.db import models

# Create your models here.

class name(models.Model):
	ticker =models.CharField(max_length=20) 
	company = models.CharField(max_length=100) 
