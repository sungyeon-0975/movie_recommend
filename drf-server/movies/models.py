from django.db import models
from django.conf import settings
from django.db.models.fields.related import ManyToManyField

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=100)
    overview = models.TextField()
    poster_path = models.CharField(max_length=200)
    release_date = models.DateField()
    vote_average = models.FloatField()
    vote_count = models.IntegerField()
    runtime = models.IntegerField()
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies')

class UserPlaylist(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class Playlist(models.Model):
    playlist_id = models.ForeignKey(UserPlaylist, on_delete=models.CASCADE)
    movie_id = models.ForeignKey(Movie,on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_playlists')
    
class Genre(models.Model):
    genre = models.CharField(max_length=50)
    movies = models.ManyToManyField(Movie, related_name='genres')
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="like_genres")

class Actor(models.Model):
    name = models.CharField(max_length=100)
    birthday = models.DateField()
    gender = models.CharField(max_length=50)
    biography = models.TextField()
    profile_path = models.CharField(max_length=200)

    starring = ManyToManyField(Movie, related_name='cast')

