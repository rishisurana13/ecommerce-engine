from rest_framework import serializers
from order.models import Order
from order.line_item_serializers import LineItemSummarySerializer

class OrderSerializer(serializers.ModelSerializer):
	order_value = serializers.SerializerMethodField()
	lineItems = LineItemSummarySerializer(many=True, read_only=True)

	class Meta:
		model = Order
		fields = ['user', 'status','lineItems', 'created', 'updated', 'url']

	def get_order_value(self, obj):
		# Ensure tax amount is added here for production iteration.
		total = 0
		# Go through all associated line items and obtain the product value
		for li in obj.lineItems.all():
			if li.product.discount == 0:
				total += li.product.price*quantity
			else:
				total += (li.product.price - (li.product.price * li.product.discount))*quantity

