from product.serializers import ProductSerializer
from rest_framework.viewsets import ModelViewSet
from permissions.permissions import IsAdminUserOrReadOnly
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from product.models import Product




class ProductViewSet(ModelViewSet):
	queryset = Product.objects.all()
	serializer_class = ProductSerializer
	permission_classes = [IsAdminUserOrReadOnly]

	def get_queryset(self):
		return self.queryset.filter(available=True)

# 




