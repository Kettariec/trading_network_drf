from rest_framework import serializers
from trading_network.models import NetworkNode, Product


class ProductSerializer(serializers.ModelSerializer):
    """Сериализатор продукта"""

    class Meta:
        model = Product
        fields = '__all__'


class NetworkNodeSerializer(serializers.ModelSerializer):
    """Сериализатор звена цепи"""

    products = ProductSerializer(many=True, read_only=True)
    level = serializers.ChoiceField(choices=NetworkNode.LEVEL)

    class Meta:
        model = NetworkNode
        fields = ['id', 'name', 'email', 'country', 'city', 'street',
                  'house_number', 'supplier', 'debt', 'created_at', 'products', 'level']
        read_only_fields = ['debt']
