from trading_network.serializers import NetworkNodeSerializer, ProductSerializer
from trading_network.models import NetworkNode, Product


def test_network_node_serializer():
    node = NetworkNode(
        name="Retailer",
        email="retailer@gmail.com",
        country="USA",
        city="New York",
        street="Wall Street",
        house_number="7",
        level=17
    )

    serializer = NetworkNodeSerializer(instance=node)
    data = serializer.data

    assert data['name'] == "Retailer"
    assert data['email'] == "retailer@gmail.com"


def test_product_serializer():
    supplier = NetworkNode(
        name="Supplier",
        email="supplier@gmail.com",
        country="USA",
        city="New York",
        street="Wall Street",
        house_number="8",
        level=18
    )

    product = Product(name="Product", model="Model 5", supplier=supplier)
    serializer = ProductSerializer(instance=product)
    data = serializer.data

    assert data['name'] == "Product"
    assert data['model'] == "Model 5"
