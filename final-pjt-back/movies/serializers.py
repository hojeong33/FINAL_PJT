from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import  Movie, Review, Genre, Director, Actor, Comment, Video,Rate, Pick
from accounts.serializers import UserSerializer


class ActorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Actor
        fields = ('id', 'name',)

class DirectorSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = Director
        fields = ('id', 'name',)

class GenreSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Genre
        fields = '__all__'

class VideoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Video
        fields = '__all__'
        
class CommentSerializer(serializers.ModelSerializer):
    user=UserSerializer(read_only=True)
    class Meta:
        model = Comment
        fields = ('id', 'review', 'user','content', 'created_at', 'updated_at',)
        read_only_fields = ('review',)
        
class ReviewSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    comments_count = serializers.IntegerField(source='comments.count', read_only=True)
    user=UserSerializer(read_only=True)
    
    class Meta:
        model = Review
        fields = ('id', 'movie', 'user', 'content', 'created_at', 'updated_at', 'comments', 'comments_count', 'title', )
        read_only_fields = ('movie',)
        
class MovieListSerializer(serializers.ModelSerializer):
    
    class Meta: 
        model = Movie
        fields = ('id', 'tmdb_id', 'title', 'poster_path', 'genres', 'popularity' )
        
class RateSerializer(serializers.ModelSerializer):
    
    user = UserSerializer(read_only=True)
    
    class Meta:
        model = Rate
        fields = ('id', 'movie', 'user', 'short_comment', 'rate')
        read_only_fields = ('movie',)

class MovieSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)
    reviews_count = serializers.IntegerField(source = 'reviews.count', read_only=True)
    videos = VideoSerializer(many=True, read_only=True)
    actors = ActorSerializer(many=True, read_only=True)
    directors = DirectorSerializer(many=True, read_only=True)
    genres = GenreSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = ('id', 'tmdb_id', 'title', 'release_date', 'popularity', 'tmdb_vote_sum', 'tmdb_vote_count', 'our_vote_sum', 'our_vote_count', 'overview', 'poster_path', 'videos', 'reviews', 'reviews_count','actors', 'genres', 'directors', 'rates',)
        
    
class PickSerializer(serializers.ModelSerializer):
    # genre=GenreSerializer(many=True,read_only=True)
    class Meta:
        model = Pick
        fields = ('id', 'user', 'movie', 'title', 'poster_path')
        read_only_fields = ('user', 'movie', 'poster_path', 'title',)