# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Valor.cantidad'
        db.alter_column(u'home_valor', 'cantidad', self.gf('django.db.models.fields.DecimalField')(max_digits=12, decimal_places=2))

    def backwards(self, orm):

        # Changing field 'Valor.cantidad'
        db.alter_column(u'home_valor', 'cantidad', self.gf('django.db.models.fields.IntegerField')())

    models = {
        u'home.anio': {
            'Meta': {'object_name': 'Anio'},
            'anio': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'home.dominio': {
            'Meta': {'object_name': 'Dominio'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        },
        u'home.edad': {
            'Meta': {'object_name': 'Edad'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'rango': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        u'home.estado': {
            'Meta': {'object_name': 'Estado'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '70'})
        },
        u'home.indicador': {
            'Meta': {'object_name': 'Indicador'},
            'dominio': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'indicadores'", 'to': u"orm['home.Dominio']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        },
        u'home.valor': {
            'Meta': {'object_name': 'Valor'},
            'anio': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['home.Anio']", 'null': 'True'}),
            'cantidad': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '2'}),
            'dominio': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['home.Dominio']", 'null': 'True'}),
            'edad': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['home.Edad']", 'null': 'True'}),
            'estado': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['home.Estado']", 'null': 'True'}),
            'genero': ('django.db.models.fields.CharField', [], {'default': "'A'", 'max_length': '1', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indicador': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['home.Indicador']", 'null': 'True'})
        }
    }

    complete_apps = ['home']