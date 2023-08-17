from django.db import models

NULLABLE={'blank':True,'null':True}

class Category(models.Model):
    name=models.CharField(max_length=100,verbose_name='Наименование')
    description = models.TextField(**NULLABLE, verbose_name='Описание')




    def __str__(self):
        return f'{self.name}'


    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Product(models.Model):
    name=models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(**NULLABLE, verbose_name='Описание')
    image=models.ImageField(upload_to='media/',**NULLABLE,verbose_name='Фото')
    category=models.ForeignKey(Category, on_delete=models.CASCADE,verbose_name='Категория')
    price=models.IntegerField(verbose_name='Цена')
    date_of_creation=models.DateTimeField(**NULLABLE,verbose_name='Дата создания')
    modified_date=models.DateTimeField(**NULLABLE,verbose_name='Дата правки')

    def __str__(self):
        return f'{self.name} {self.price} {self.description}'

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товавры'
