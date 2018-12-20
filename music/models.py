from django.db import models
from django.urls import reverse


class Album(models.Model):
    artist = models.CharField(max_length=20)
    album_title = models.CharField(max_length=20)
    genre = models.CharField(max_length=20)
    album_logo = models.CharField(max_length=100)
    is_favorite = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('music:details', kwargs={'pk': self.pk, })

    def __str__(self):
        return self.album_title+' '+self.artist

    class Meta:
        db_table = 'Album'


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    song_title = models.CharField(max_length=50)
    file_type = models.CharField(max_length=10)
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.song_title+'.'+self.file_type

    class Meta:
        db_table = 'Song'
