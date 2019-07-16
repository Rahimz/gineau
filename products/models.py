from django.db import models
from django.utils import timezone



class Product(models.Model):
	STATUS_CHOICES = (
    ('men', 'Men'),
    ('women', 'Women'),
    )
	productName = models.CharField(max_length=250)
	productGenre = models.CharField(max_length=50,
									choices=STATUS_CHOICES, 
									default='draft')
	productGroup = models.CharField(max_length=250)
	productSize = models.CharField(max_length=250)
	productDescript = models.TextField()
	productImage = models.FileField(null=True, blank=True)
	imageAlt = models.CharField(max_length=250,
								null=True,
								blank=True)
	productPublish = models.DateTimeField('date published')


	def __str__(self):
		return self.productName


class Image(models.Model):
	product = models.ForeignKey(Product,
								related_name='image',
								on_delete=models.CASCADE)
	#productName = self.productName
	image = models.ImageField(null=True, blank=True)
	votes = models.IntegerField(default=0)

	def __str__(self):
		return str(self.product_id)


class Email(models.Model):
	email = models.EmailField()
	created = models.DateTimeField(auto_now_add=True)


	def __str__(self):
		return str(self.email)