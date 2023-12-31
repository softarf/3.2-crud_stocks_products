# Generated by Django 4.2.4 on 2023-08-04 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logistic', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['title'], 'verbose_name': 'Товар', 'verbose_name_plural': 'Товары'},
        ),
        migrations.AlterModelOptions(
            name='stock',
            options={'ordering': ['name'], 'verbose_name': 'Склад', 'verbose_name_plural': 'Склады'},
        ),
        migrations.AddField(
            model_name='stock',
            name='name',
            field=models.CharField(default='z', max_length=20, verbose_name='Название'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(max_length=60, unique=True, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='address',
            field=models.CharField(max_length=200, unique=True, verbose_name='Адрес склада'),
        ),
    ]
