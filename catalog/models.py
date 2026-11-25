from django.db import models


class Category(models.Model):
    """Модель для описания категорий товаров"""
    name = models.CharField(max_length=50, verbose_name='Наименование категории', help_text='Введите наименование категории')
    description = models.TextField(verbose_name='Описание категории', blank=True, null=True, help_text='Введите описание категории')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    """Модель для описания товаров"""
    name = models.CharField(max_length=50, verbose_name='Наименование товара', help_text='Введите наименование товара')
    description = models.TextField(verbose_name='Описание товара', blank=True, null=True, help_text='Введите описание товара')
    image = models.ImageField(upload_to='products/', blank=True, null=True, verbose_name='Фотография товара')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', verbose_name='Категория')
    price = models.IntegerField(verbose_name='Цена за покупку товара', help_text='Введите цену за покупку товара')
    created_at = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateField(auto_now=True, verbose_name='Последнее изменение')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ["name"]
