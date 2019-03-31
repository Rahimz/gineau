from django.db import models

# Create your models here.


class Product(models.Model):
	productName = models.CharField(max_length=250)
	productGenre = models.CharField(max_length=250)
	productGroup = models.CharField(max_length=250)
	productSize = models.CharField(max_length=250)
	productDescript = models.CharField(max_length=250)
	productImage = models.FileField(null=True, blank=True)
	productPublish = models.DateTimeField('date published')


	def __str__(self):
		return self.productName


class Image(models.Model):
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	#productName = self.productName
	imageMain = models.FileField(null=True, blank=True)
	votes = models.IntegerField(default=0)

	def __str__(self):
		return str(self.imageMain) + ' - ' + str(self.product_id)

'''
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0
    '''
