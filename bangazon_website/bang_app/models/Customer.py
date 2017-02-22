from django.db import models
from django.contrib.auth.models import User

import sys 
sys.path.append('../') 

import datetime



class Customer(models.Model):
	"""
	Purpose: Create a Customer
	Author: Abby
	Methods: str - returns first and last name
		
	"""
	user = models.OneToOneField(User, on_delete=models.CASCADE) 
	date = models.DateTimeField(default=datetime.now, blank=True)
	street_address = models.CharField(max_length=70)
	city = models.CharField(max_length=70)
	state = models.CharField(max_length=70)
	zip_code = models.CharField(max_length=10)


	def __str__(self):
	return "{} {}".format(self.user.first_name, self.user.last_name)

	

