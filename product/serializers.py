from rest_framework import serializers

from product.models import Product




class ProductSerializer(serializers.ModelSerializer):
	
	
	class Meta:
		model = Product
		fields = ['id', 'title', 'price','discount','final_price', 'quantity', 'product_type', 'url', 'quantity','description', 'available']
		

	def validate(self, data):
		product_type = data['product_type']
		quantity = data['quantity']
		discount = float(data['discount'])
			
		if int(quantity) == 0:
			data['available'] = False
		else:
			data['available'] = True

		if discount > 1 or discount < 0:
			raise serializers.ValidationError('Discount can only be a value between 0 and 1.')

		return data
		





		




