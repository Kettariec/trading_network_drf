from rest_framework import viewsets, permissions
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from .models import NetworkNode, Product
from .serializers import NetworkNodeSerializer, ProductSerializer


class IsActiveEmployee(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.is_active


class NetworkNodeViewSet(viewsets.ModelViewSet):
    """'Эндпоинт звена сети"""
    queryset = NetworkNode.objects.all()
    serializer_class = NetworkNodeSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['country']
    search_fields = ['city']
    permission_classes = [IsActiveEmployee]


class ProductViewSet(viewsets.ModelViewSet):
    """'Эндпоинт продукта"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsActiveEmployee]
