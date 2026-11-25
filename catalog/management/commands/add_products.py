from django.core.management.base import BaseCommand
from catalog.models import Product, Category

class Command(BaseCommand):
    help = 'add test products to the database'

    def handle(self, *args, **options):
        Product.objects.all().delete()
        Category.objects.all().delete()

        cat_1, _ = Category.objects.get_or_create(name='smartphones', description='powerful and smart')

        products = [
            {'name': 'iphone 18 pro max', 'price': 100000, 'category': cat_1},
            {'name': 'xiaomi redmi note 7', 'price': 50000, 'category': cat_1},
            {'name': 'samsung galaxy 20', 'price': 100000, 'category': cat_1},
        ]

        for product_data in products:
            product, created = Product.objects.get_or_create(**product_data)
            if created:
                self.stdout.write(self.style.SUCCESS(f'В базу данных успешно записан {product}'))
            else: # никогда не выполнится, это на случай если в список словарей попадут одинаковые словари
                self.stdout.write(self.style.WARNING(f"{product} уже существует в базе данных"))




