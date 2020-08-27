from django.db import models
from datetime import datetime
from realtors.models import Realtor

class Listing(models.Model):
	is_published = models.BooleanField(default=True)
	title = models.CharField(max_length=200)
	list_date = models.DateField(default=datetime.now ,blank=True)	
	category = models.CharField(max_length=300,default='Private')
	language = models.CharField(max_length=300,default='Private')	
	framework = models.CharField(max_length=300,default='Private')
	features = models.TextField(blank=True)
	description = models.TextField(blank=True)	
	photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
	photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
	photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
	photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
	photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
	photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
	photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
	photo_7 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
	photo_8 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
	photo_9 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
	photo_10 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
	photo_11 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
	photo_12 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
	photo_13 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
	photo_14 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
	photo_15 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)	
	realtor = models.ForeignKey(Realtor, on_delete = models.DO_NOTHING,default='Private')

	def __str__(self):
		return self.title

