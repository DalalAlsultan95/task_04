from django.db import models

# Create your models here.
class Restaurant(models.Model):
	name = models.CharField(max_length=35)
	description = models.CharField(max_length=240)
	opening_time = models.TimeField()
	closing_time = models.TimeField()