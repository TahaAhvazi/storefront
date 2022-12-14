from django.contrib import admin
from . import models

@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'unit_price', 'inventory_status', 'collection']
    list_editable = ['unit_price']
    list_per_page: int = 10
    @admin.display(ordering='inventory')
    def inventory_status(self, product):
        if product.inventory < 10 :
            return 'Low'
        return 'Ok'

admin.site.register(models.Collection)

@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'membership']
    list_editable = ['membership']
    list_per_page: int = 10
    search_fields = ['first_name__istartswith', 'last_name']

@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'placed_at', 'customer']
