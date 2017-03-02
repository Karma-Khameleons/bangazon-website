from django.contrib import admin
from bang_app import models

admin.site.register(models.Customer)
admin.site.register(models.ProductType)
admin.site.register(models.Product)
admin.site.register(models.PaymentType) 
admin.site.register(models.CustomerOrder) 
admin.site.register(models.LineItem) 