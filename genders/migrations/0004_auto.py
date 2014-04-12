# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing M2M table for field albun on 'Gender'
        db.delete_table(db.shorten_name(u'genders_gender_albun'))

        # Adding M2M table for field album on 'Gender'
        m2m_table_name = db.shorten_name(u'genders_gender_album')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('gender', models.ForeignKey(orm[u'genders.gender'], null=False)),
            ('album', models.ForeignKey(orm[u'albums.album'], null=False))
        ))
        db.create_unique(m2m_table_name, ['gender_id', 'album_id'])


    def backwards(self, orm):
        # Adding M2M table for field albun on 'Gender'
        m2m_table_name = db.shorten_name(u'genders_gender_albun')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('gender', models.ForeignKey(orm[u'genders.gender'], null=False)),
            ('album', models.ForeignKey(orm[u'albums.album'], null=False))
        ))
        db.create_unique(m2m_table_name, ['gender_id', 'album_id'])

        # Removing M2M table for field album on 'Gender'
        db.delete_table(db.shorten_name(u'genders_gender_album'))


    models = {
        u'albums.album': {
            'Meta': {'object_name': 'Album'},
            'artist': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['artists.Artist']"}),
            'cover': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'artists.artist': {
            'Meta': {'object_name': 'Artist'},
            'biography': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['artists.Country']", 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_group': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'artists.country': {
            'Meta': {'object_name': 'Country'},
            'continent': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'genders.gender': {
            'Meta': {'object_name': 'Gender'},
            'album': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'+'", 'blank': 'True', 'to': u"orm['albums.Album']"}),
            'artist': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'+'", 'blank': 'True', 'to': u"orm['artists.Artist']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'track': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'+'", 'blank': 'True', 'to': u"orm['tracks.Track']"})
        },
        u'tracks.track': {
            'Meta': {'object_name': 'Track'},
            'album': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['albums.Album']"}),
            'artist': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['artists.Artist']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'track_field': ('django.db.models.fields.files.FileField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['genders']