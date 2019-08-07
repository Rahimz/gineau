from django.db import models
from django.utils import timezone
from taggit.managers import TaggableManager



class Product(models.Model):
	STATUS_CHOICES = (
    				  ('men', 'Men'),
					  ('women', 'Women'),
					 )
	GROUP_CHOICES = (
				     ('handbag', 'Handbag'),
					 ('backpack', 'Backpack'),
					 ('purse', 'Purse'),
					 ('accessory', 'Accessory'),
					 ('bag', 'Bag'),
					 ('briefcase', 'Briefcase'),
					 ('wallet', 'Wallet'),					 
	)
	productName = models.CharField(max_length=250)
	productGenre = models.CharField(max_length=50,
									choices=STATUS_CHOICES, 
									default='women')
	productGroup = models.CharField(max_length=250,
									choices=GROUP_CHOICES,
									default='handbag')									
	productSize = models.CharField(max_length=250)
	productSizeH = models.IntegerField(null=True,
									   blank=True,
									   verbose_name='Height')
	productSizeW = models.IntegerField(null=True,
									   blank=True,
									   verbose_name='Width')
	productSizeD = models.IntegerField(null=True,
									   blank=True,
									   verbose_name='Depth')									   
	productDescript = models.TextField()
	productImage = models.FileField(null=True, blank=True)
	imageAlt = models.CharField(max_length=250,
								null=True,
								blank=True)
	productPublish = models.DateTimeField('date published')


	tags = TaggableManager()

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
	

	def __str__(self):
		return str(self.email)