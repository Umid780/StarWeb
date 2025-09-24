from django.contrib import admin
from .models import Car, Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('brand', 'model', 'year', 'price')
    search_fields = ('brand','model','vin')