from django.db import models

class ProductType(models.Model):
	label = models.CharField(max_length=30)

	class Meta:
		verbose_name_plural = 'ProductTypes'

	def __str__(self):
		return '{}'.format(self.label)