from django.shortcuts import render
from rest_framework import authentication, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from .models import Category, MenuItem, Cart, Order, OrderItem
from .serializers import MenuItemSerializer
#Auth imports
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User, Group
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from .serializers import UserSerializer

# Create your views here.

# Create functions to match endpoint in the description
# Original Djoser endpoint is auth/users/me
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def current_user(request):
    serializer = UserSerializer(request.user)
    return Response(serializer.data)

#Original Djoser to return token auth/token/login
@api_view(['POST'])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)

    if not user:
        return Response({"error": 'Invalid User or Password'}, status=status.HTTP_401_UNAUTHORIZED)

    token, _ = Token.objects.get_or_create(user=user)
    return Response({'auth_token': token.key})


@api_view(['GET', 'POST'])
def menu_items(request):
    items = MenuItem.objects.all()
    serialized_item = MenuItemSerializer(items, many=True)
    return Response(serialized_item.data)
