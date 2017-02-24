from django.db import models
from django.contrib.auth.models import User
import datetime

# A class needs a view and url to connect the dots

class Customer(models.Model):
	"""
	Purpose: Create a Customer
	Author: Abby
	Methods: str - returns first and last name
		
	"""
	user = models.OneToOneField(User, on_delete=models.CASCADE) 
	street_address = models.CharField(max_length=50)
	city = models.CharField(max_length=50)
	state = models.CharField(max_length=25)
	zip_code = models.CharField(max_length=10)


	def __str__(self):
		return "{}".format(self.user.first_name)

	class Meta:
		app_label="bang_app"

	

