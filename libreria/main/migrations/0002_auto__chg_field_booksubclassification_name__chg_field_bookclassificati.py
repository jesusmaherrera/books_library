# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'BookSubClassification.name'
        db.alter_column('main_booksubclassification', 'name', self.gf('django.db.models.fields.CharField')(max_length=40))

        # Changing field 'BookClassification.name'
        db.alter_column('main_bookclassification', 'name', self.gf('django.db.models.fields.CharField')(max_length=40))

    def backwards(self, orm):

        # Changing field 'BookSubClassification.name'
        db.alter_column('main_booksubclassification', 'name', self.gf('django.db.models.fields.CharField')(max_length=25))

        # Changing field 'BookClassification.name'
        db.alter_column('main_bookclassification', 'name', self.gf('django.db.models.fields.CharField')(max_length=25))

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
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        },
        'main.booksubclassification': {
            'Meta': {'object_name': 'BookSubClassification'},
            'book_clasification': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.BookClassification']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40'})
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