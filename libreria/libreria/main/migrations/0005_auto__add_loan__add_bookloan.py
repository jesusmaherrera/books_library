# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Loan'
        db.create_table('main_loan', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.User'], null=True, on_delete=models.SET_NULL, blank=True)),
            ('loan_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('delivery_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('loan_type', self.gf('django.db.models.fields.CharField')(default='C', max_length=10)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal('main', ['Loan'])

        # Adding model 'BookLoan'
        db.create_table('main_bookloan', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('loan', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Loan'], null=True, on_delete=models.SET_NULL, blank=True)),
            ('book', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Book'], null=True, on_delete=models.SET_NULL, blank=True)),
            ('state', self.gf('django.db.models.fields.CharField')(default='N', max_length=10)),
        ))
        db.send_create_signal('main', ['BookLoan'])


    def backwards(self, orm):
        # Deleting model 'Loan'
        db.delete_table('main_loan')

        # Deleting model 'BookLoan'
        db.delete_table('main_bookloan')


    models = {
        'main.book': {
            'Meta': {'object_name': 'Book'},
            'autor': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'book_classification': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.BookClassification']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'book_subclassification': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.BookSubClassification']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'donor': ('django.db.models.fields.CharField', [], {'max_length': '35'}),
            'editorial': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'exemplar': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'volume': ('django.db.models.fields.CharField', [], {'max_length': '15'})
        },
        'main.bookclassification': {
            'Meta': {'object_name': 'BookClassification'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'main.bookloan': {
            'Meta': {'object_name': 'BookLoan'},
            'book': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Book']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'loan': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Loan']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'default': "'N'", 'max_length': '10'})
        },
        'main.booksubclassification': {
            'Meta': {'object_name': 'BookSubClassification'},
            'book_clasification': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.BookClassification']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'main.guarantor': {
            'Meta': {'object_name': 'Guarantor'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'age': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'institution': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'occupation': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'postal_code': ('django.db.models.fields.CharField', [], {'max_length': '5'})
        },
        'main.loan': {
            'Meta': {'object_name': 'Loan'},
            'delivery_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'loan_date': ('django.db.models.fields.DateTimeField', [], {}),
            'loan_type': ('django.db.models.fields.CharField', [], {'default': "'C'", 'max_length': '10'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.User']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'})
        },
        'main.user': {
            'Meta': {'object_name': 'User'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'age': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'guarantor': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Guarantor']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'institution': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'institution_userid': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'occupation': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'postal_code': ('django.db.models.fields.CharField', [], {'max_length': '5'})
        }
    }

    complete_apps = ['main']