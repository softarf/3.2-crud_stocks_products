from rest_framework.viewsets import ModelViewSet

from logistic.models import Product, Stock
from logistic.serializers import ProductSerializer, StockSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # lookup_field = 'id'                  # По умолчанию показ отдельного продукта выполняется по его "id". - '/2/'
    # Задаёт типы фильтров.
    search_fields = ['title', 'description']    # Поиск по включению в содержимом поля. - '/?search=Помид'
    ordering_fields = ['id', 'title']           # Упорядочивание по полю модели. - '/?ordering=title,-id'


class StockViewSet(ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    lookup_field = 'name'                # Показ отдельного склада выполняется по его названию. - '/Центральный/'
    # Задаёт типы фильтров.
    search_fields = ['id']               # Поиск по включению в содержимом поля.
    ordering_fields = ['id', 'name']     # Упорядочивание по указанному полю модели.

    def get_queryset(self):
        """ Поиск складов, где есть определённый продукт. """
        queryset = Stock.objects.all()
        product_id = self.request.query_params.get('product')

        if product_id:

            queryset = queryset.filter(products__id=product_id)           # Вариант 1

            # queryset = Product.objects.get(id=product_id).stocks.all()    # Вариант 2

        return queryset
