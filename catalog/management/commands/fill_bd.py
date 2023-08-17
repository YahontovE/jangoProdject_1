from django.core.management import BaseCommand

import json

from catalog.models import Category


class Command(BaseCommand):
    def handle(self, *args, **options):
        category_list = [
            {'name': 'Спортивные товары'},
            {'name': 'Товары для дома'},
            {'name': 'Инвентарь для тениса'},
            {'name': 'Озежда'},
            {'name': 'Обувь'}

        ]

        category_for_create=[]
        for category_item in category_list:
            category_for_create.append(
                Category(**category_item)
            )
        Category.objects.all().delete()
        Category.objects.bulk_create(category_for_create)
