from django.contrib import admin
from .models import Category, Product

# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Класс для определения отображения продуктов в админке"""
    list_display = ('id', "name", 'price', 'category')
    list_filter = ('category', )
    search_fields = ('name', 'description')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Класс для определения отображения категорий в админке"""
    list_display = ('id', "name")
    search_fields = ('name', 'description')

