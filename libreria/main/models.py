#encoding:utf-8
from django.db import models

#BOOKS
class BookClassification(models.Model):
	name = models.CharField(max_length=50)
	image = models.ImageField(blank=True, null=True, upload_to='bookClassifications', verbose_name='Imágen')

	def __unicode__(self):
		return self.name

class BookSubClassification(models.Model):
	name = models.CharField(max_length=50)
	book_clasification = models.ForeignKey(BookClassification, on_delete=models.SET_NULL, blank=True, null=True)
	image = models.ImageField(blank=True, null=True, upload_to='bookSubClassifications', verbose_name='Imágen')

	def __unicode__(self):
		return self.name

class Book(models.Model):
	code = models.CharField(max_length=25)
	name = models.CharField(max_length=50)
	image = models.ImageField(blank=True, null=True, upload_to='books', verbose_name='Imágen')
	book_classification = models.ForeignKey(BookClassification, on_delete= models.SET_NULL, blank=True, null=True)
	book_subclassification = models.ForeignKey(BookSubClassification, on_delete= models.SET_NULL, blank=True, null=True)
	autor = models.CharField(max_length=50)
	volume = models.CharField(max_length=15)
	exemplar = models.CharField(max_length=15)
	editorial = models.CharField(max_length=30)
	description = models.CharField(max_length=60)
	location = models.CharField(max_length=30)
	donor = models.CharField(max_length=35)

	def __unicode__(self):
		return self.code
#USERS

class Guarantor(models.Model):
	name = models.CharField(max_length=40)
	age = models.CharField(max_length=3)
	address = models.CharField(max_length=60)
	postal_code = models.CharField(max_length=5)
	phone = models.CharField(max_length=10)
	occupation = models.CharField(max_length=30)
	institution = models.CharField(max_length=30)

	def __unicode__(self):
		return self.name
		
class User(models.Model):
	name = models.CharField(max_length=40)
	age = models.CharField(max_length=3)
	address = models.CharField(max_length=60)
	postal_code = models.CharField(max_length=5)
	phone = models.CharField(max_length=10)
	occupation = models.CharField(max_length=30)
	institution = models.CharField(max_length=30)
	institution_userid = models.CharField(max_length=10)
	guarantor = models.ForeignKey(Guarantor, on_delete=models.SET_NULL, blank=True, null=True)

	def __unicode__(self):
		return self.name