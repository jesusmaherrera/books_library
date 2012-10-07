#encoding:utf-8
from django import forms
from main.models import *

class BookManageForm(forms.ModelForm):
	class Meta:
		model = Book

class BookClassificationManageForm(forms.ModelForm):
	class Meta:
		model = BookClassification
	 