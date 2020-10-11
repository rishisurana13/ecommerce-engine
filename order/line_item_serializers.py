from rest_framework import serializers
from order.models import LineItem

class AttrPKField(serializers.PrimaryKeyRelatedField):
    def get_queryset(self):
        user = self.context['request'].user.user
        queryset = Order.objects.filter(user=user).filter(status='checkout')
        return queryset

class LineItemSummarySerializer(serializers.ModelSerializer):

	order = AttrPKField()
	final_price = serializers.SerializerMethodField()
	product_title = serializers.SerializerMethodField()


	class Meta:
		model = LineItem
		fields = ['product_title', 'final_price', 'quantity', 'order', 'url']

	
	def get_final_price(self, obj):
		if obj.product.discount == 0:
			return obj.product.price * obj.quantity
		else:
			return quantity * (obj.product.price - (obj.product.price - obj.product.discount))
	def get_product_title(self, obj):
		return obj.product.title


	def validate_quantity(self, value):
		if value == 0:
			raise serializers.ValidationError("Quantity cannot be 0.")
		
		return value

	def validate(self, data):
		if bool(data['available']) == False:
			raise serializers.ValidationError("Product not available.") 
		return data


