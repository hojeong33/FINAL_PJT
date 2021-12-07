from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .serializers import UserSerializer,UserProfileSerializer
from django.contrib.auth import get_user_model

User=get_user_model()

@api_view(['POST'])
@permission_classes([AllowAny])
def signup(request):
    password=request.data.get('password')
    password_confirmation=request.data.get('passwordConfirmation')

    if password !=password_confirmation:
        return Response ({'error':'비밀번호가 일치하지 않습니다.'}, status=status.HTTP_400_BAD_REQUEST)

    if User.objects.filter(username=request.data.get('username')).exists():
        return Response ({'error':'이미 사용중인 아이디입니다.'},status=status.HTTP_400_BAD_REQUEST)

    if User.objects.filter(email=request.data.get('email')).exists():
        return Response({'error':'이미 사용중인 이메일입니다.'},status=status.HTTP_400_BAD_REQUEST)
    
    serializer=UserSerializer(data=request.data)

    if serializer.is_valid(raise_exception=True):
        user=serializer.save()

        user.set_password(request.data.get('password'))
        user.save()

    return Response(serializer.data,status=status.HTTP_201_CREATED)
    
@api_view(['GET','PUT','DELETE'])
def profile(request):
    if request.method=='GET':
        serializer=UserProfileSerializer(request.user)
        return Response(serializer.data)
