# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'BookClassification'
        db.create_table('main_bookclassification', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=25)),
        ))
        db.send_create_signal('main', ['BookClassification'])

        # Adding model 'BookSubClassification'
        db.create_table('main_booksubclassification', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('book_clasification', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.BookClassification'], null=True, on_delete=models.SET_NULL, blank=True)),
        ))
        db.send_create_signal('main', ['BookSubClassification'])

        # Adding model 'Book'
        db.create_table('main_book', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('book_classification', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.BookClassification'], null=True, on_delete=models.SET_NULL, blank=True)),
            ('book_subclassification', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.BookSubClassification'], null=True, on_delete=models.SET_NULL, blank=True)),
            ('autor', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('volume', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('exemplar', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('editorial', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('donor', self.gf('django.db.models.fields.CharField')(max_length=35)),
        ))
        db.send_create_signal('main', ['Book'])

        # Adding model 'Guarantor'
        db.create_table('main_guarantor', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('age', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('postal_code', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('occupation', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('institution', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal('main', ['Guarantor'])

        # Adding model 'User'
        db.create_table('main_user', (
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
        db.send_create_signal('main', ['User'])


    def backwards(self, orm):
        # Deleting model 'BookClassification'
        db.delete_table('main_bookclassification')

        # Deleting model 'BookSubClassification'
        db.delete_table('main_booksubclassification')

        # Deleting model 'Book'
        db.delete_table('main_book')

        # Deleting model 'Guarantor'
        db.delete_table('main_guarantor')

        # Deleting model 'User'
        db.delete_table('main_user')


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
            'location': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'volume': ('django.db.models.fields.CharField', [], {'max_length': '15'})
        },
        'main.bookclassification': {
            'Meta': {'object_name': 'BookClassification'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '25'})
        },
        'main.booksubclassification': {
            'Meta': {'object_name': 'BookSubClassification'},
            'book_clasification': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.BookClassification']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '25'})
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