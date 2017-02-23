from django.contrib import admin

# Register your models here.
from django.contrib import admin
from bang_app import models

# @admin.register(models.Customer, models.ProductType, models.Product, models.PaymentType, models.Order)



admin.site.register(models.Customer)
admin.site.register(models.ProductType)
admin.site.register(models.Product)
admin.site.register(models.PaymentType)