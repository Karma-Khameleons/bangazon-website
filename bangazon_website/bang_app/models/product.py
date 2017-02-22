from django.db import models
from .customer import Customer
from .product_type import ProductType


class Product(models.Model):

	'''
		Puprose-
			maintain relevant information to product
		Methods-

		@rtwhitfield84

	'''

	name = models.CharField(max_length=100)
	price = models.CharField(max_length=20)
	description = models.CharField(max_length=500)
	quantity = models.PositiveIntegerField(default=1)
	product_type = models.ForeignKey(ProductType, on_delete=models.CASCADE)
	seller = models.ForeignKey(Customer, on_delete=models.CASCADE)

	class Meta:
		verbose_name_plural = 'Products'
		fields = ('name', 'price', 'description', 'seller')
