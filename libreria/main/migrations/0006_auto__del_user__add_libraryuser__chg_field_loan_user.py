# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'User'
        db.delete_table('main_user')

        # Adding model 'LibraryUser'
        db.create_table('main_libraryuser', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('age', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('postal_code', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('occupation', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('institution', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('institution_userid', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('guarantor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Guarantor'], null=True, on_delete=models.SET_NULL, blank=True)),
        ))
        db.send_create_signal('main', ['LibraryUser'])


        # Changing field 'Loan.user'
        db.alter_column('main_loan', 'user_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.LibraryUser'], null=True, on_delete=models.SET_NULL))

    def backwards(self, orm):
        # Adding model 'User'
        db.create_table('main_user', (
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('postal_code', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('institution', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('occupation', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('institution_userid', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('age', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('guarantor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Guarantor'], null=True, on_delete=models.SET_NULL, blank=True)),
        ))
        db.send_create_signal('main', ['User'])

        # Deleting model 'LibraryUser'
        db.delete_table('main_libraryuser')


        # Changing field 'Loan.user'
        db.alter_column('main_loan', 'user_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.User'], null=True, on_delete=models.SET_NULL))

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
        'main.libraryuser': {
            'Meta': {'object_name': 'LibraryUser'},
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
        },
        'main.loan': {
            'Meta': {'object_name': 'Loan'},
            'delivery_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'loan_date': ('django.db.models.fields.DateTimeField', [], {}),
            'loan_type': ('django.db.models.fields.CharField', [], {'default': "'C'", 'max_length': '10'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.LibraryUser']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'})
        }
    }

    complete_apps = ['main']