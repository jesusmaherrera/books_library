from libreria.main.models import Book, BookClassification, BookSubClassification, Loan
from django.contrib import admin

admin.site.register(Book)
admin.site.register(Loan)
admin.site.register(BookClassification)
admin.site.register(BookSubClassification)
