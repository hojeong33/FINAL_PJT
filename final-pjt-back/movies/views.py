from django.contrib.auth import get_user_model
import requests
from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework import serializers
from rest_framework.serializers import Serializer
from .models import  Movie, Review, Genre, Director, Actor, Comment, Video, Rate, Pick
from .serializers import MovieListSerializer, MovieSerializer, ActorSerializer, DirectorSerializer, ReviewSerializer, GenreSerializer, CommentSerializer, VideoSerializer, RateSerializer, PickSerializer
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from django.core.paginator import Paginator
from django.db.models import F
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import AllowAny
from pprint import pprint



User=get_user_model()

# Create your views here.
# 메인 페이지
# 영화 조회
@api_view(['GET'])
def get_movies_all(request):
    mode=request.GET.get('mode')
    if mode=='release_date':
        movies = Movie.objects.order_by('-release_date')
    elif mode=='popularity':
        movies = Movie.objects.order_by('-popularity')
    elif mode=='vote_average':
        movies = Movie.objects.annotate(vote_average=(F('tmdb_vote_sum') + F('our_vote_sum')) / (F('tmdb_vote_count') + F('our_vote_count'))).order_by('-vote_average')
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)


# 영화 상세 페이지
# 단일 영화 정보
@api_view(['GET'])
def get_movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)

# 감독 정보
@api_view(['GET'])
def get_directors_all(request, movie_pk):
    directors = Director.objects.filter(director_movie_pk=movie_pk)
    serializer = DirectorSerializer(directors, many=True)
    return Response(serializer.data)

# 배우 정보
@api_view(['GET'])
def get_actors_all(request, movie_pk):
    actors = Actor.objects.filter(actor_movie_pk=movie_pk)
    serializer = ActorSerializer(actors, many=True)
    return Response(serializer.data)

# 영상 정보
@api_view(['GET'])
def get_videos_all(request, movie_pk):
    videos = Video.objects.filter(pk = movie_pk)
    serializer = VideoSerializer(videos, many=True)
    return Response(serializer.data)

# 내 리뷰 가져오기
@api_view(['GET'])
def get_my_reviews(request,user_pk):
    if request.method=='GET':
        reviews = Review.objects.filter(user_id=user_pk).order_by('-pk')
        serializer=ReviewSerializer(reviews,many=True)
        data=serializer.data
        return Response(data)

# 내 댓글 가져오기
@api_view(['GET'])
def get_my_comments(request,user_pk):
    if request.method=='GET':
        comments = Comment.objects.filter(user_id=user_pk).order_by('-pk')
        serializer=CommentSerializer(comments,many=True)
        data=serializer.data
        return Response(data)

#내가 좋아요한 영화 가져오기
@api_view(['GET'])
def get_my_movies(request,user_pk):
    if request.method=='GET':
        pick_list= Pick.objects.filter(user_id=user_pk).order_by('-pk')
        serializer = PickSerializer(pick_list, many=True)
        data = serializer.data
        return Response(data)

# 영화 좋아요
@api_view(['GET', 'POST', 'DELETE'])
def pick_movie(request, movie_pk):
    if request.method == 'GET':
        pick_movie = Pick.objects.filter(user__pk=request.user.pk, movie__pk=movie_pk).first()
        serializer = PickSerializer(pick_movie)
        print(serializer)
        return Response(serializer.data)
    elif request.method == 'POST':
        movie = get_object_or_404(Movie, pk=movie_pk)
        serializer = PickSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user, movie=movie, poster_path=movie.poster_path, title=movie.title)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    elif request.method == 'DELETE':
        photo_ticket = Pick.objects.filter(user__pk=request.user.pk, movie__pk=movie_pk).first()
        photo_ticket.delete()
        data = {
            'delete' : '좋아요 해제'
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)

# 리뷰 조회 및 생성
@api_view(['GET', 'POST'])
def get_reviews_all(request, movie_pk):
    movie = get_object_or_404(Movie, pk = movie_pk)
    # 리뷰 읽기(페이지네이터 사용)
    if request.method == 'GET':
        reviews = Review.objects.filter(movie_id=movie_pk).order_by('-pk')
        # paginator = Paginator(reviews, 5)
        # page = request.GET.get('page_num')
        # reviews = paginator.get_page(page)
        serializer = ReviewSerializer(reviews, many=True)
        # data = serializer.data
        # data.append({'possible_page': paginator.num_pages})
        return Response(serializer.data)

    # 리뷰 생성
    elif request.method == 'POST':
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user, movie=movie)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


# # 리뷰 삭제 및 수정
@api_view(['GET', 'DELETE', 'PUT'])
def get_review_detail(request, review_pk):
    review = get_object_or_404(Review, pk = review_pk)
    
    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        return Response(serializer.data)
    
    # 리뷰를 작성한 유저와 요청한 유저가 같을 때 수정 및 삭제 가능
    elif request.user == review.user:
        # 리뷰 삭제
        if request.method == 'DELETE':
            review.delete()
            data = {
                'delete': f'{review_pk}번 리뷰가 삭제되었습니다.'
            }
            return Response(data, status=status.HTTP_204_NO_CONTENT)
        # 리뷰 수정
        elif request.method == 'PUT':
            serializer = ReviewSerializer(review, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
    
    # 리뷰를 작성한 유저와 요청한 유저가 달라 권한이 없다
    return Response({ 'Unauthorized': '권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)


    
# # 댓글 조회 및 생성
@api_view(['GET', 'POST'])
def get_comments_all(request, review_pk):
    review = get_object_or_404(Review, pk = review_pk)
    
    if request.method == 'GET':
        comments = Comment.objects.filter(review_id=review_pk).order_by('-pk')
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user, review=review)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


# # 댓글 삭제 및 수정
@api_view(['DELETE', "PUT"])
def get_comment_detail(request, comment_pk):
    comment = get_object_or_404(Comment, pk = comment_pk)
    
    if request.user == comment.user:
        if request.method == 'DELETE':
            comment.delete()
            data ={
                'delete' : f'{comment_pk}번 댓글이 삭제되었습니다.'
            }
            return Response(data, status=status.HTTP_204_NO_CONTENT)
        
        elif request.method == 'PUT':
            serializer = CommentSerializer(comment, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
   
    return Response({ 'Unauthorized': '권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)


# 평점 조회 및 생성
@api_view(['GET', 'POST'])
def get_rates_all(request, movie_pk):
    movie = get_object_or_404(Movie,pk=movie_pk)
    if request.method == 'GET':
        rates = Rate.objects.filter(movie_id = movie_pk).order_by('pk')
        serializer = RateSerializer(rates, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = RateSerializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user, movie=movie)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

# 평점 수정 삭제
@api_view(['GET','DELETE', 'PUT'])
def get_rate_detail(request, rate_pk):
    rate = get_object_or_404(Rate, pk =rate_pk)
    
    if request.method == 'GET':
        serializer = RateSerializer(rate)
        return Response(serializer.data)
    
    if request.user == rate.user:
        if request.method == 'DELETE':
            rate.delete()
            data ={
                'delete' : f'{rate_pk}번 댓글이 삭제되었습니다.'
            }
            return Response(data, status=status.HTTP_204_NO_CONTENT)

        elif request.method == 'PUT':
            serializer = RateSerializer(rate, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
   
    return Response({ 'Unauthorized': '권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)
    # # 리뷰를 작성한 유저와 요청한 유저가 같을 때 수정 및 삭제 가능
    # elif request.user == review.user:
    #     # 리뷰 삭제
    #     if request.method == 'DELETE':
    #         review.delete()
    #         data = {
    #             'delete': f'{review_pk}번 리뷰가 삭제되었습니다.'
    #         }
    #         return Response(data, status=status.HTTP_204_NO_CONTENT)
    #     # 리뷰 수정
    #     elif request.method == 'PUT':
    #         serializer = ReviewSerializer(review, data=request.data)
    #         if serializer.is_valid(raise_exception=True):
    #             serializer.save()
    #             return Response(serializer.data)
    
    # # 리뷰를 작성한 유저와 요청한 유저가 달라 권한이 없다
    # return Response({ 'Unauthorized': '권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)    

###########################
# db 저장
## 장르
@api_view(['POST'])
@permission_classes([AllowAny])
def upload_genres_all(request):
    # if request.data.get('username') == 'admin'
    
    API_KEY = 'cf85387cb23102d7dcdbb033efadd2e5' # 최종 제출 전에 숨기기
    url = f'https://api.themoviedb.org/3/genre/movie/list?api_key={API_KEY}&region=KR&language=ko'
    res = requests.get(url).json()
    
    for data in res.get('genres'):
        Genre.objects.create(
            tmdb_genre_id = data.get('id'),
            name = data.get('name'),
        )
    
    # # 대규모로 만들때는 bulk_create
    # Genre.objects.bulk_create(
    #     [Genre(
    #        genre_id = data.get('id'),
    #        name = data.get('name'),
    #         ) for data in res.get('genres')]
    # )

    return Response({ 'database' : '성공적으로 데이터를 등록했습니다.'})
    # return Response({ 'Unauthorized': '권한이 없습니다'}, status=status.HTTP_403_FORBIDDEN)

## 영화 정보
@api_view(['POST'])
@permission_classes([AllowAny])
def upload_movies_all(request):
    # if request.data.get('username') == 'admin'
    API_KEY = 'cf85387cb23102d7dcdbb033efadd2e5'
    for page in range(1, 31):
        url = f'https://api.themoviedb.org/3/movie/popular?api_key={API_KEY}&page={page}&region=KR&language=ko'
        res = requests.get(url).json()
        
        for data in res.get('results'):
            if Movie.objects.filter(title=data.get('title')).exists():
                movie = Movie.objects.get(title=data.get('title'))
                movie.popularity = data.get('popularity')
                movie.tmdb_vote_sum = data.get('vote_average') * data.get('vote_count')
                movie.tmdb_vote_count = data.get('vote_count')
                movie.save()
            else: 
                movie = Movie.objects.create(
                    tmdb_id = data.get('id'),
                    title = data.get('title'),
                    release_date = data.get('release_date'),
                    popularity = data.get('popularity'),
                    tmdb_vote_sum = float(data.get('vote_average')) * float(data.get('vote_count')),
                    tmdb_vote_count = data.get('vote_count'),
                    our_vote_sum = 0,
                    our_vote_count = 0,
                    overview =  data.get('overview'),
                    poster_path = 'https://image.tmdb.org/t/p/w500' + data.get('poster_path'),
                    # video_path = '',
                    # runtime = data.get('runtime')
                )
                for genre_id in data.get('genre_ids'):
                    genre = Genre.objects.get(tmdb_genre_id = genre_id)
                    genre.movies.add(movie)
                    
    return Response({ 'database' : '성공적으로 데이터를 등록했습니다.'})
    # return Response({ 'Unauthorized': '권한이 없습니다'}, status=status.HTTP_403_FORBIDDEN)

## 감독, 배우
@api_view(['POST'])
@permission_classes([AllowAny])
def upload_credits_all(request):
    # if request.data.get('username') == 'admin'
    API_KEY = 'cf85387cb23102d7dcdbb033efadd2e5'
    movies = get_list_or_404(Movie)
    
    for movie in movies:
        url = f'https://api.themoviedb.org/3/movie/{movie.tmdb_id}/credits?api_key={API_KEY}&region=KR&language=ko'
        res = requests.get(url).json()
        
        for credits in res.get('cast')[:5]:
            if not Actor.objects.filter(name=credits.get('name')).exists() and credits.get('known_for_department') == 'Acting':
                actor = Actor.objects.create(name=credits.get('name'))
                actor.movies.add(movie)
        
        for credits in res.get('crew'):
            if not Director.objects.filter(name=credits.get('name')).exists() and credits.get('job') == 'Director':
                director = Director.objects.create(name=credits.get('name'))
                director.movies.add(movie)    
    
    return Response({ 'database' : '성공적으로 데이터를 등록했습니다.'})
    
    # return Response({ 'Unauthorized': '권한이 없습니다'}, status=status.HTTP_403_FORBIDDEN)

## 비디오 키
@api_view(['POST'])
@permission_classes([AllowAny])
def upload_videos_all(request):
     # if request.data.get('username') == 'admin'
    API_KEY = 'cf85387cb23102d7dcdbb033efadd2e5'
    movies = get_list_or_404(Movie)
    
    for movie in movies:
        url = f'https://api.themoviedb.org/3/movie/{movie.tmdb_id}/videos?api_key={API_KEY}&region=KR'
        res = requests.get(url).json()
        
        for videos in res.get('results'):
            if not Video.objects.filter(video_keys=videos.get('key')).exists() and videos.get('type') == 'Trailer':
                video = Video.objects.create(video_keys=videos.get('key'), movie_id=movie.id)
                
    return Response({ 'database' : '성공적으로 데이터를 등록했습니다.'})            
    # return Response({ 'Unauthorized': '권한이 없습니다'}, status=status.HTTP_403_FORBIDDEN)


