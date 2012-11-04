#encoding:utf-8
from django import forms
from main.models import *
from django.forms.models import BaseInlineFormSet, inlineformset_factory

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

class LoanManageForm(forms.ModelForm):
	class Meta:
		model = Loan

class BookLoanManageForm(forms.ModelForm):
	model = BookLoan

def get_bookloan_items_formset(form, formset = BaseInlineFormSet, **kwargs):
	return inlineformset_factory(Loan, BookLoan, form, formset, **kwargs)