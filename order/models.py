from django.db import models
from user.models import User
from product.models import Product
# Create your models here.
STATUS_CHOICES = (
	('checkout', 'Checkout'),
	('success', 'Success'),
	('failure', 'Failure'),
	('refunded', 'Refunded'),
	)

class Order(models.Model):
	user = models.ForeignKey(User, related_name='orders', on_delete=models.CASCADE)
	status = models.CharField(max_length=64, choices=STATUS_CHOICES, default='checkout')
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)	
	

	def __str__(self): 
		return self.id + ' ' + self.status


class LineItem(models.Model):
	# Using the product relation we can determine its final price
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	quantity = models.PositiveIntegerField()
	order = models.ForeignKey(Order,  related_name='line_items',on_delete=models.CASCADE)

	def __str__(self):
		return self.product.title  