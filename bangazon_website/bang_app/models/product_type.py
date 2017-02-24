from django.db import models
import sqlite3

class ProductType(models.Model):
	'''
		Purpose-
			maintain information relevant to ProductType

		@rtwhitfield84
	'''
	label = models.CharField(max_length=30)

	class Meta:
		verbose_name_plural = 'ProductTypes'

	def get_product_categories():
		categories = ProductType.objects.all()
		return categories
		# food = ProductType("groceries")
		# electronics = ProductType("electronics")
		# furniture = ProductType("furniture")
		# category_list = [food, electronics, furniture]
		# return category_list

	def __str__(self):
		return '{}'.format(self.label)