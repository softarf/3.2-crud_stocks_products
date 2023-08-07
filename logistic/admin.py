from django.contrib import admin

from logistic.models import Product, Stock


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description')
    list_display_links = ('id', 'title', 'description')
    search_fields = ('id', 'title', 'description')


@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'address')
    list_display_links = ('id', 'name', 'address')
    search_fields = ('id', 'name', 'address')
