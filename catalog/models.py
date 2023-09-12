from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(**NULLABLE, verbose_name='Описание')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(**NULLABLE, verbose_name='Описание')
    image = models.ImageField(upload_to='media/', **NULLABLE, verbose_name='Фото')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    price = models.IntegerField(verbose_name='Цена')
    date_of_creation = models.DateTimeField(**NULLABLE, verbose_name='Дата создания')
    modified_date = models.DateTimeField(**NULLABLE, verbose_name='Дата правки')

    def __str__(self):
        return f'{self.name} {self.price} {self.description}'

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товавры'

class Blog(models.Model):
    header = models.CharField(max_length=100, verbose_name='Заголовок')
    slug = models.CharField(max_length=150, **NULLABLE, verbose_name='slug')
    content = models.TextField(verbose_name='Контент')
    prevuew = models.ImageField(**NULLABLE, verbose_name='Изображение')
    date_create = models.DateTimeField(**NULLABLE, verbose_name='Дата создания')
    is_published = models.BooleanField(default=True, verbose_name='Опубликованно')
    views_count = models.IntegerField(default=0, verbose_name='Просмотры')

    def __str__(self):
        return f'{self.header} {self.content}'

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'

class Version(models.Model):
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    num_ver=models.IntegerField(verbose_name='номер версии')
    name_ver=models.CharField(max_length=150,**NULLABLE,verbose_name='название версии')
    valid_ver=models.BooleanField(verbose_name='признак текущей версии')

    def __str__(self):
        return f'{self.num_ver}'

    class Meta:
        verbose_name = 'Версия'
        verbose_name_plural = 'Версии'