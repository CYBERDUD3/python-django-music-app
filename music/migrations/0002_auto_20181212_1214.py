# Generated by Django 2.1.4 on 2018-12-12 06:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='album',
            old_name='albumlogo',
            new_name='album_logo',
        ),
        migrations.RenameField(
            model_name='album',
            old_name='albumtitle',
            new_name='album_title',
        ),
        migrations.RenameField(
            model_name='song',
            old_name='filetype',
            new_name='file_type',
        ),
        migrations.RenameField(
            model_name='song',
            old_name='isfavorite',
            new_name='is_favorite',
        ),
        migrations.RenameField(
            model_name='song',
            old_name='song',
            new_name='song_title',
        ),
    ]
