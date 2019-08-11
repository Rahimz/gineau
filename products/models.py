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
	#TODO:: Ading thumbnail for slideshow
	image1 = models.ImageField(null=True, blank=True)
	image2 = models.ImageField(null=True, blank=True)
	image3 = models.ImageField(null=True, blank=True)
	image4 = models.ImageField(null=True, blank=True)
	image5 = models.ImageField(null=True, blank=True)
	imageAlt = models.CharField(max_length=250,
								null=True,
								blank=True)
	votes = models.IntegerField(default=0)
	
	productPublish = models.DateTimeField('date published')


	tags = TaggableManager()

	def __str__(self):
		return self.productName


class Slider(models.Model):
	title = models.CharField(max_length=250)
	description = models.CharField(max_length=500)
	image = models.ImageField(upload_to='slider/')
	active = models.BooleanField(default=True)

	def __str__(self):
		return self.title

class Image(models.Model):
	product = models.OneToOneField(Product,
								related_name='image',
								on_delete=models.CASCADE)
	#productName = self.productName
	image1 = models.ImageField(null=True, blank=True)
	image2 = models.ImageField(null=True, blank=True)
	image3 = models.ImageField(null=True, blank=True)
	image4 = models.ImageField(null=True, blank=True)
	image5 = models.ImageField(null=True, blank=True)
	votes = models.IntegerField(default=0)

	def __str__(self):
		return str(self.product.productName)


class Email(models.Model):
	email = models.EmailField()
	date = models.DateTimeField()

	def __str__(self):
		return str(self.email)