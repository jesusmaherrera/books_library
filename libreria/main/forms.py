#encoding:utf-8
from django import forms
from main.models import *

class BookManageForm(forms.ModelForm):
	class Meta:
		model = Book

class BookClassificationManageForm(forms.ModelForm):
	class Meta:
		model = BookClassification

class LibraryUserManageForm(forms.ModelForm):
	class Meta:
		model = LibraryUser	 

class GuarantorManageForm(forms.ModelForm):
	class Meta:
		model = Guarantor