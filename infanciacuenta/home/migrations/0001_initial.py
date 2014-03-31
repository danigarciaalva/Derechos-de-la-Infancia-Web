# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Estado'
        db.create_table(u'home_estado', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=70)),
        ))
        db.send_create_signal(u'home', ['Estado'])

        # Adding model 'Anio'
        db.create_table(u'home_anio', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('anio', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'home', ['Anio'])

        # Adding model 'Dominio'
        db.create_table(u'home_dominio', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=500)),
        ))
        db.send_create_signal(u'home', ['Dominio'])

        # Adding model 'Indicador'
        db.create_table(u'home_indicador', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('dominio', self.gf('django.db.models.fields.related.ForeignKey')(related_name='indicadores', to=orm['home.Dominio'])),
        ))
        db.send_create_signal(u'home', ['Indicador'])

        # Adding model 'Edad'
        db.create_table(u'home_edad', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('rango', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal(u'home', ['Edad'])

        # Adding model 'Valor'
        db.create_table(u'home_valor', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('estado', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['home.Estado'], null=True)),
            ('anio', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['home.Anio'], null=True)),
            ('dominio', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['home.Dominio'], null=True)),
            ('indicador', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['home.Indicador'], null=True)),
            ('edad', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['home.Edad'], null=True)),
            ('cantidad', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'home', ['Valor'])


    def backwards(self, orm):
        # Deleting model 'Estado'
        db.delete_table(u'home_estado')

        # Deleting model 'Anio'
        db.delete_table(u'home_anio')

        # Deleting model 'Dominio'
        db.delete_table(u'home_dominio')

        # Deleting model 'Indicador'
        db.delete_table(u'home_indicador')

        # Deleting model 'Edad'
        db.delete_table(u'home_edad')

        # Deleting model 'Valor'
        db.delete_table(u'home_valor')


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
            'cantidad': ('django.db.models.fields.IntegerField', [], {}),
            'dominio': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['home.Dominio']", 'null': 'True'}),
            'edad': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['home.Edad']", 'null': 'True'}),
            'estado': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['home.Estado']", 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indicador': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['home.Indicador']", 'null': 'True'})
        }
    }

    complete_apps = ['home']