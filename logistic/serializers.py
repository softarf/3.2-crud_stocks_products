from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from logistic.models import Product, StockProduct, Stock


class ProductSerializer(serializers.ModelSerializer):
    """ Задаёт сериализатор для продукта."""

    class Meta:
        model = Product                            # Связанная модель.
        fields = ['id', 'title', 'description']    # Обрабатываемые поля.


class ProductPositionSerializer(serializers.ModelSerializer):
    """ Задаёт сериализатор для позиции продукта на складе. """

    class Meta:
        model = StockProduct                                        # Связанная модель.
        fields = ['id', 'product', 'quantity', 'price']    # Обрабатываемые поля.


class StockSerializer(serializers.ModelSerializer):
    """ Задаёт сериализатор для склада """

    positions = ProductPositionSerializer(read_only=True, many=True, required=False)

    class Meta:
        model = Stock                                      # Связанная модель.
        fields = ['id', 'name', 'address', 'positions']    # Обрабатываемые поля.

    def create(self, validated_data):
        # Достаёт связанные данные для другой таблицы (StockProduct).
        positions = validated_data.pop('positions', [])    # Тип 'positions' - список из упорядоченных словарей.

        # Создаёт склад по его параметрам.
        stock = super().create(validated_data)

        for position in positions:
            # Добавляет товары на склад (заполняет связанную таблицу StockProduct).
            position['stock_id'] = stock.id
            StockProduct.objects.create(**position)

        return stock

    def update(self, instance, validated_data):
        # Достаёт связанные данные для другой таблицы (StockProduct).
        positions = validated_data.pop('positions', [])

        # Обновляет склад по его параметрам.
        stock = super().update(instance, validated_data)

        for position in positions:
            # Добавляет товары на склад (меняет связанную таблицу StockProduct).
            StockProduct.objects.update_or_create(stock=stock,
                                                   product=position['product'],
                                                   defaults={'quantity': position['quantity'],
                                                             'price': position['price']
                                                   })
        return stock
