from rest_framework.viewsets import ModelViewSet

from logistic.models import Product, Stock
from logistic.serializers import ProductSerializer, StockSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'title'                      # Показ отдельного продукта выполняется по его названию.
    # Задаёт типы фильтров.
    search_fields = ['title', 'description']    # Поиск по включению в содержимом поля.
    ordering_fields = ['id', 'title']           # Упорядочивание по полю модели.


class StockViewSet(ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    lookup_field = 'name'                # Показ отдельного склада выполняется по его названию.
    # Задаёт типы фильтров.
    search_fields = ['id']               # Поиск по включению в содержимом поля.
    ordering_fields = ['id', 'name']     # Упорядочивание по указанному полю модели.
