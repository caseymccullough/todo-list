from django.db import models

class Artist (models.Model):
    name = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100)
    photo_url = models.TextField()

    def __str__ (self):
        return self.name

class Song (models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name="songs") # if this song is deleted, delete all links to this song
    title = models.CharField(max_length=100, default="untitled")
    album = models.CharField(max_length=100, default="untitled")
    preview_url = models.TextField(null=True)

    def __str__ (self):
        return self.title
