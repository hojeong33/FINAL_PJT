from django.db import models
from django.conf import settings
from django.db.models.fields import FloatField
from django.core.validators import MaxValueValidator, MinValueValidator

class Movie(models.Model):
    tmdb_id = models.IntegerField()
    title = models.CharField(max_length=100)
    release_date = models.DateField()
    popularity = models.FloatField()
    tmdb_vote_sum = models.FloatField()
    tmdb_vote_count = models.IntegerField()
    our_vote_sum = models.IntegerField()
    our_vote_count = models.IntegerField()
    overview = models.TextField()
    poster_path = models.TextField()
    # like_users=models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='like_articles')
    # videos = models.ForeignKey(Videos, on_delete=models.CASCADE, related_name='movies')
    # runtime = models.IntegerField()
    
    def __str__(self):
        return self.title

class Genre(models.Model):
    movies = models.ManyToManyField(Movie, related_name='genres')
    tmdb_genre_id = models.IntegerField()
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class Director(models.Model):
    movies = models.ManyToManyField(Movie, related_name='directors')
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Actor(models.Model):
    movies = models.ManyToManyField(Movie, related_name='actors')
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Video(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='videos')
    video_keys = models.CharField(max_length=100)
    
    def __str__(self):
        return self.video_keys

class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reviews')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_opened=models.BooleanField(default=False)
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.content


class Rate(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='rates')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='rates')
    rate = models.FloatField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    short_comment = models.CharField(max_length=100)
    
    def __str__(self):
        return f'평점: {self.rate} / 한줄평: {self.short_comment}'
    
class Pick(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='my_movies')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='pick_user')
    title = models.CharField(max_length=100)
    poster_path = models.TextField()
    
