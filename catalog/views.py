from django.shortcuts import render

from catalog.models import Product


def home(request):
    catalog_list = Product.objects.all()
    context = {
        'object_list': catalog_list,
        'title': 'семейный магазин'
    }
    return render(request, 'catalog/home.html', context)


def contact_info(request):
    context = {
        'title': 'Контакты'
    }
    return render(request, 'catalog/contact_info.html', context)


def product(request, pk):
    category_items = Product.objects.get(pk=pk)
    context = {
        'object_list': Product.objects.filter(category_id=pk),
        'title': 'семейный магазин',
        'titel_2': category_items

    }
    return render(request, 'catalog/product.html', context)
