# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Track.order'
        db.add_column(u'tracks_track', 'order',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=None),
                      keep_default=False)

        # Adding field 'Track.track_field'
        db.add_column(u'tracks_track', 'track_field',
                      self.gf('django.db.models.fields.files.FileField')(default=1, max_length=100),
                      keep_default=False)

        # Adding field 'Track.album'
        db.add_column(u'tracks_track', 'album',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['albums.Album']),
                      keep_default=False)

        # Adding field 'Track.artist'
        db.add_column(u'tracks_track', 'artist',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['artists.Artist']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Track.order'
        db.delete_column(u'tracks_track', 'order')

        # Deleting field 'Track.track_field'
        db.delete_column(u'tracks_track', 'track_field')

        # Deleting field 'Track.album'
        db.delete_column(u'tracks_track', 'album_id')

        # Deleting field 'Track.artist'
        db.delete_column(u'tracks_track', 'artist_id')


    models = {
        u'albums.album': {
            'Meta': {'object_name': 'Album'},
            'artist': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['artists.Artist']"}),
            'cover': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'artists.artist': {
            'Meta': {'object_name': 'Artist'},
            'biography': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'tracks.track': {
            'Meta': {'object_name': 'Track'},
            'album': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['albums.Album']"}),
            'artist': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['artists.Artist']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'track_field': ('django.db.models.fields.files.FileField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['tracks']