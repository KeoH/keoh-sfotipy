# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Country'
        db.create_table(u'artists_country', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('continent', self.gf('django.db.models.fields.CharField')(max_length=2, blank=True)),
        ))
        db.send_create_signal(u'artists', ['Country'])

        # Adding field 'Artist.country'
        db.add_column(u'artists_artist', 'country',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['artists.Country'], blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'Country'
        db.delete_table(u'artists_country')

        # Deleting field 'Artist.country'
        db.delete_column(u'artists_artist', 'country_id')


    models = {
        u'artists.artist': {
            'Meta': {'object_name': 'Artist'},
            'biography': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['artists.Country']", 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'artists.country': {
            'Meta': {'object_name': 'Country'},
            'continent': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['artists']