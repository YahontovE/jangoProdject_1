# Generated by Django 4.2.4 on 2023-09-16 10:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_version'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='version',
            options={'verbose_name': 'Версия', 'verbose_name_plural': 'Версии'},
        ),
    ]
