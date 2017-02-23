from django.db import models
from .customer import Customer
from .product_type import ProductType


class Product(models.Model):

	'''
		Puprose-
			maintain information relevant to product

		@rtwhitfield84

	'''

	name = models.CharField(max_length=100)
	price = models.DecimalField(max_digits=20, decimal_places=2)
	description = models.CharField(max_length=500)
	quantity = models.PositiveIntegerField(default=1)
	product_type = models.ForeignKey(ProductType, on_delete=models.CASCADE)
	seller = models.ForeignKey(Customer, on_delete=models.CASCADE)

	class Meta:
		verbose_name_plural = 'Products'
	
	def __str__(self):
		return '{} {} {}'.format(self.name, self.price, self.description)
