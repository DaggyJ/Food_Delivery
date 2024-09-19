from django.contrib import admin
from . import models
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','title', 'description', 'selling_price', 'discounted_price']
    search_fields = ['title', 'description']
    list_filter = ['selling_price', 'discounted_price']

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'locality', 'city','mobile','zipcode']
    search_fields = ['user', 'locality', 'city']

admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.Customer, CustomerAdmin)