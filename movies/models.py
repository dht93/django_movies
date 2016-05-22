from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=50)
    year = models.IntegerField(default=0, null=True)
    director = models.CharField(max_length=50, null=True)
    genre = models.CharField(max_length=50, null=True)
    poster_url = models.CharField(max_length=50, null=True)
    tomatometer = models.IntegerField(default=0, null=True)
    imdb_rating = models.FloatField(default=0, null=True)
    seen_status = models.BooleanField(default=False)
    bookmarked = models.BooleanField(default=False)
    def __unicode__(self):
        return self.title
