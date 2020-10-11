from django.db import models


FILE_TYPE_CHOICES = (
	("Trousers", "Trousers"), ("Shirt", "Shirt"), ("Shoes", "Shoes"), ("Accessory", "Accessory"), ("Hoodie/Sweater", "Hoodie/Sweater"),\
	("Trackpants", "Trackpants"), ("Tee", "Tee"), 
	)

class Product(models.Model):
	title = models.CharField(max_length=164, unique=True)
	price = models.DecimalField(max_digits=5,decimal_places=2)
	product_type = models.CharField(max_length=164,choices=FILE_TYPE_CHOICES)
	discount = models.DecimalField(max_digits=3,decimal_places=2,blank=True) 
	quantity = models.PositiveIntegerField(blank=True,null=True)
	description = models.TextField(blank=True)
	# product_image = models.ImageField(blank=True)
	available = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)


	def __str__(self):
		return self.title








	










