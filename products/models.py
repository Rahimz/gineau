from django.db import models
from django.utils import timezone
from taggit.managers import TaggableManager
from django.urls import reverse



class Product(models.Model):
	STATUS_CHOICES = (('men', 'Men'),
					  ('women', 'Women'),
					  )
	GROUP_CHOICES = (('handbag', 'Handbag'),
					 ('backpack', 'Backpack'),
					 ('purse', 'Purse'),
					 ('accessory', 'Accessory'),
					 ('bag', 'Bag'),
					 ('briefcase', 'Briefcase'),
					 ('wallet', 'Wallet'),					 
	)
	productName = models.CharField(max_length=250)
	slug = models.SlugField(max_length=250, unique=True)
	productGenre = models.CharField(max_length=50,
									choices=STATUS_CHOICES,
									default='women')
	productGroup = models.CharField(max_length=250,
									choices=GROUP_CHOICES,
									default='handbag')									
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
	productImage = models.FileField(upload_to='products',
									null=True, blank=True)
	imageAlt = models.CharField(max_length=500,null=True, blank=True)
	# Images of slideshow
	image1 = models.ImageField(upload_to='products',
							   null=True, blank=True)
	image1_thumb = models.ImageField(upload_to='thumbnails',
									 null=True, blank=True)
	image1_alt = models.CharField(max_length=500,null=True, blank=True)
	
	image2 = models.ImageField(upload_to='products',
							   null=True, blank=True)
	image2_thumb = models.ImageField(upload_to='thumbnails',
									 null=True, blank=True)
	image2_alt = models.CharField(max_length=500,null=True, blank=True)
	
	image3 = models.ImageField(upload_to='products',
							   null=True, blank=True)
	image3_thumb = models.ImageField(upload_to='thumbnails',
									 null=True, blank=True)	
	image3_alt = models.CharField(max_length=500,null=True, blank=True)

	image4 = models.ImageField(upload_to='products',
							   null=True, blank=True)
	image4_thumb = models.ImageField(upload_to='thumbnails',
									 null=True, blank=True)
	image4_alt = models.CharField(max_length=500,null=True, blank=True)

	image5 = models.ImageField(upload_to='products',
							   null=True, blank=True)
	image5_thumb = models.ImageField(upload_to='thumbnails',
									 null=True, blank=True)
	image5_alt = models.CharField(max_length=500,null=True, blank=True)
	
	votes = models.IntegerField(default=0)
	
	productPublish = models.DateTimeField(auto_now_add=True)
	
	
	
	tags = TaggableManager()
	
	def get_absolute_url(self):
		return reverse('products:detail', args=[self.slug])

	def __str__(self):
		return self.productName


class Slider(models.Model):
	product = models.ForeignKey(Product,
								on_delete=models.CASCADE,
								null=True, 
								blank=True,)
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