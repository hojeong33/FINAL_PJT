from django.contrib import admin
from .models import Movie, Review, Genre, Director, Actor, Comment,Rate,Video,Pick

# Register your models here.
admin.site.register(Movie)
admin.site.register(Review)
admin.site.register(Genre)
admin.site.register(Director)
admin.site.register(Actor)
admin.site.register(Comment)
admin.site.register(Rate)
admin.site.register(Video)
admin.site.register(Pick)