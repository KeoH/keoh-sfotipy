# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Gender.albun'
        db.delete_column(u'genders_gender', 'albun_id')

        # Deleting field 'Gender.artist'
        db.delete_column(u'genders_gender', 'artist_id')

        # Adding M2M table for field albun on 'Gender'
        m2m_table_name = db.shorten_name(u'genders_gender_albun')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('gender', models.ForeignKey(orm[u'genders.gender'], null=False)),
            ('album', models.ForeignKey(orm[u'albums.album'], null=False))
        ))
        db.create_unique(m2m_table_name, ['gender_id', 'album_id'])

        # Adding M2M table for field artist on 'Gender'
        m2m_table_name = db.shorten_name(u'genders_gender_artist')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('gender', models.ForeignKey(orm[u'genders.gender'], null=False)),
            ('artist', models.ForeignKey(orm[u'artists.artist'], null=False))
        ))
        db.create_unique(m2m_table_name, ['gender_id', 'artist_id'])


    def backwards(self, orm):
        # Adding field 'Gender.albun'
        db.add_column(u'genders_gender', 'albun',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['albums.Album']),
                      keep_default=False)

        # Adding field 'Gender.artist'
        db.add_column(u'genders_gender', 'artist',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['artists.Artist']),
                      keep_default=False)

        # Removing M2M table for field albun on 'Gender'
        db.delete_table(db.shorten_name(u'genders_gender_albun'))

        # Removing M2M table for field artist on 'Gender'
        db.delete_table(db.shorten_name(u'genders_gender_artist'))


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
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'genders.gender': {
            'Meta': {'object_name': 'Gender'},
            'albun': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'+'", 'symmetrical': 'False', 'to': u"orm['albums.Album']"}),
            'artist': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'+'", 'symmetrical': 'False', 'to': u"orm['artists.Artist']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['genders']