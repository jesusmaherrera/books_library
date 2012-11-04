#encoding:utf-8
from django.db import models
from datetime import datetime 

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
		return self.name

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
		
class LibraryUser(models.Model):
	name = models.CharField(max_length=40)
	age = models.CharField(max_length=3)
	#DIRECCION
	address = models.CharField(max_length=60)
	postal_code = models.CharField(max_length=5)
	
	phone = models.CharField(max_length=10)

	occupation = models.CharField(max_length=30)
	institution = models.CharField(max_length=30)
	institution_userid = models.CharField(max_length=10, blank=True, null=True)
	
	guarantor = models.ForeignKey(Guarantor, on_delete=models.SET_NULL, blank=True, null=True)

	def __unicode__(self):
		return self.name

class Loan(models.Model):
	user = models.ForeignKey(LibraryUser, on_delete=models.SET_NULL, blank=True, null=True)
	loan_date = models.DateTimeField(default=datetime.now(),blank=True)
	delivery_date = models.DateTimeField(default=datetime.now(), blank=True, null=True)
	LOAN_TYPE = (
		('L', 'LIBRO'),
		('LD', 'LIBRO A DOMICILIO'),
		('C', 'COMPUTADORA'),
		)
	loan_type = models.CharField(max_length=10, choices=LOAN_TYPE, default='C')
	description = models.CharField(max_length=100,blank= True, null =True)

class BookLoan(models.Model):
	loan = models.ForeignKey(Loan, on_delete=models.SET_NULL, blank=True, null=True)
	book = models.ForeignKey(Book, on_delete=models.SET_NULL, blank=True, null=True)
	BOOK_STATE = (
		('B', 'BUENO'),
		('N', 'NORMAL'),
		)
	state = models.CharField(max_length=10, choices=BOOK_STATE,
		default='N')