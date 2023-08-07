from django.core.management.base import BaseCommand
from logistic.models import Stock

""" Предназначается для прямого удаления заданного склада из БД.
    Применяется на этапе отладки проекта.
"""


class Command(BaseCommand):
    help = 'Ручное удаления заданного склада'

    def add_arguments(self, parser):
        """ Получает название удаляемого склада. """
        parser.add_argument(
            'stock_name',
            action='store',
            nargs='?',
            help='Название удаляемого склада'
        )

    def handle(self, *args, **options):
        """ Удаляет склад с названием stock_name.
            Вместе с ним автоматически удаляются ссылки на товары на этом складе (on_delete=models.CASCADE).
        """
        stock = Stock.objects.get(name=options['stock_name'])
        stock.delete()

        self.stdout.write(f"Склад '{stock.name}' удалён")  # Для теста.
