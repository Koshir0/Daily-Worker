from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
	job = models.CharField(max_length=100, blank = True, null=True)
	gender = models.CharField(max_length=10, blank = True, null=True)
	title = models.CharField(max_length=10, blank = True, null=True)
	phone = models.CharField(max_length=15, blank = True, null=True)
	picture = models.CharField(max_length=500, blank = True, null=True)
	country = models.CharField(max_length=100, blank = True, null=True)
	nat = models.CharField(max_length=10, blank = True, null=True)

	def __str__(self):
		return self.username


class tools(models.Model):
	tool = models.CharField(max_length=100, blank = True, null=True)
	desc = models.CharField(max_length=100, blank = True, null=True)
	price = models.IntegerField()
	image = models.CharField(max_length=200, blank = True, null=True)
	country = models.CharField(max_length=100, blank = True, null=True)
	owner = models.CharField(max_length=100, blank = True, null=True)
	is_rented = models.CharField( max_length=5, null=True, default="false" )


	def __str__(self):
		return self.tool

class Reserve(models.Model):
	tool = models.CharField(max_length=100, blank = True, null=True)
	renter = models.CharField(max_length=100, blank = True, null=True)
	place = models.CharField(max_length=100, blank = True, null=True)
	days = models.IntegerField()


	def __str__(self):
		return f"Tool: {self.tool}, Renter: {self.renter}"