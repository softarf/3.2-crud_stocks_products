from django.core.validators import MinValueValidator
from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=60, unique=True, verbose_name='Название')
    description = models.TextField(null=True, blank=True,verbose_name='Описание')
    #
    objects = models.Manager()      # Диспетчер записей.

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['title']

    def __str__(self):
        return self.title


class Stock(models.Model):
    name = models.CharField(max_length=20, verbose_name='Название')
    address = models.CharField(max_length=200, unique=True, verbose_name='Адрес склада')
    products = models.ManyToManyField(
        Product,
        through='StockProduct',
        related_name='stocks',
    )
    #
    objects = models.Manager()      # Диспетчер записей.

    class Meta:
        verbose_name = 'Склад'
        verbose_name_plural = 'Склады'
        ordering = ['name']

    def __str__(self):
        return f'Склад "{self.name}", адрес: {self.address[:30]}'


class StockProduct(models.Model):
    stock = models.ForeignKey(
        Stock,
        on_delete=models.CASCADE,
        related_name='positions',
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='positions',
    )
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(
        max_digits=18,
        decimal_places=2,
        validators=[MinValueValidator(0)],
    )
    #
    objects = models.Manager()      # Диспетчер записей.
