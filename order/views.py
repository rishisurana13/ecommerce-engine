from rest_framework.viewsets import ModelViewSet
from order.order_serializers import OrderSerializer 
from order.line_item_serializers import LineItemSummarySerializer 
from order.models import Order, LineItem


class LineItemViewSet(ModelViewSet):
	queryset = LineItem.objects.all()

	"""
	Edge cases to handle:
	1) Ensure ONE order only has checkout status for cart functionality
		a) an Order with checkout status is created upon account creation
		b) after checkout a new order with checkout status is created.
	2) If a line item already exists then simply update the value by incrementing the quantity
	3) 
	"""

	def get_queryset(self):
		return self.queryset.filter(order__status='checkout')

	def create(self, request, *args, **kwargs):
		orders = Order.objects.all().filter(order__user=self.request.user, status='checkout')
		data = request.data.copy()
		prod_targ = Product.objects.get(id=int(data["product"]))
		li_quant = int(data["quantity"])
		prod_quant = prod_targ.quantity

		# Edge Case test: Delete for production
		if len(orders) > 1:
			raise serializers.ValidationErro('Too many checkout orders. FU')

		# Check if item is already in Cart
		for order in orders:
			for li in orders.line_items.all():
				if li.product.id == prod_targ.id:
					instance = LineItem.objects.get(id=li.id)
					instance.quantity = instance.quantity + int(data["quantity"]) 
					instance.save()
					return Response(status=status.HTTP_200_OK)

		

		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		self.perform_create(serializer)
		headers = self.get_success_headers(serializer.data)
		return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
