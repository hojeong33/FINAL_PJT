from django.urls import path
from . import views

# app_name = 'movies'

urlpatterns = [
    path('movies/', views.get_movies_all),
    path('movies/<int:movie_pk>/',views.get_movie_detail),
    path('movies/<int:movie_pk>/directors/', views.get_directors_all),
    # path('directors/<int:director_pk>/', views.get_director_detail),
    path('movies/<int:movie_pk>/actors/', views.get_actors_all),
    # path('actors/<int:actor_pk>/', views.get_actor_detail),
    path('movies/<int:movie_pk>/reviews/', views.get_reviews_all),
    path('reviews/<int:review_pk>/', views.get_review_detail),
    path('reviews/<int:review_pk>/comments/', views.get_comments_all),
    path('comments/<int:comment_pk>/', views.get_comment_detail),
    path('movies/<int:movie_pk>/videos/',views.get_videos_all),
    path('movies/<int:movie_pk>/rates/', views.get_rates_all),
    path('rates/<int:rate_pk>/', views.get_rate_detail),
    path('myreviews/<int:user_pk>/',views.get_my_reviews),
    path('mycomments/<int:user_pk>/',views.get_my_comments),
    path('mymovies/<int:user_pk>/',views.get_my_movies),
    path('pick/<int:movie_pk>/',views.pick_movie),
    path('db/genres/', views.upload_genres_all),
    path('db/movies/', views.upload_movies_all),
    path('db/credits/', views.upload_credits_all),  
    path('db/videos/', views.upload_videos_all),
    

]
