from django.shortcuts import render, get_object_or_404
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
from django.db.models import Q

# Create your views here.

# Create functions to match endpoint in the description
# Original Djoser endpoint is auth/users/me
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def current_user(request):
    user = request.user
    return Response({"username":user.username, "password":user.email})

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


@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
@permission_classes([IsAuthenticated])
def menu_items(request):
    if request.method == 'GET':
        items = MenuItem.objects.all()
        serialized_item = MenuItemSerializer(items, many=True)
        return Response(serialized_item.data)

    if not request.user.groups.filter(name='Manager').exists():
        return Response({'message':'You are not authorized'},
                        status=status.HTTP_403_FORBIDDEN)

    if request.method == 'POST':
        serialized_item = MenuItemSerializer(data=request.data)
        if serialized_item.is_valid():
            serialized_item.save()
            return Response(serialized_item.data, status=status.HTTP_201_CREATED)
        return Response(serialized_item.errors, status=status.HTTP_400_BAD_REQUEST)

    # Handle other methods (PUT/PATCH/DELETE)
    return Response(
        {"message": "Method not allowed here - use /menu-items/<id>/"},
        status=status.HTTP_405_METHOD_NOT_ALLOWED
    )

@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
@permission_classes([IsAuthenticated])
def single_menu_item(request, pk):
    if request.method == 'GET':
        item = get_object_or_404(MenuItem, pk=pk)
        serialized_item = MenuItemSerializer(item)
        return Response(serialized_item.data)

    if not request.user.groups.filter(name='Manager').exists():
        return Response({"message": "You are not authorized"},
                        status=status.HTTP_403_FORBIDDEN)

    item = get_object_or_404(MenuItem, pk=pk)

    if request.method == 'POST':
        return Response({"message": "Use /menu-items/ for create new item"},
                        status=status.HTTP_405_METHOD_NOT_ALLOWED)

    elif request.method in ['PUT', 'PATCH']:
        serialized_item = MenuItemSerializer(
            item,
            data=request.data,
            partial=request.method == 'PATCH'
        )
        if serialized_item.is_valid():
            serialized_item.save()
            return Response(serialized_item.data)
        return Response(serialized_item.errors,
                        status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def groups_view(request):
    if not request.user.groups.filter(name='Manager').exists():
        return Response({'message':'You not authorized'},
                        status=status.HTTP_403_FORBIDDEN)

    try:
        manager_group = Group.objects.get(name='Manager')
        managers = User.objects.filter(groups=manager_group)
        manager_data = [
            {
                'id': manager.pk,
                'username': manager.username,
                'email': manager.email,
            }
            for manager in managers
        ]
        return Response(manager_data)
    except Group.DoesNotExist:
        return Response({'message':'Group does not exist'},
                        status=status.HTTP_404_NOT_FOUND)

@api_view()
@permission_classes([IsAuthenticated])
def managers(request):
    username = request.data['username']
    if username:
        user = get_object_or_404(User, username=username)
        mnanagers = Group.objects.get(name="Manager")
        if request.method == 'POST':
            managers.user.set.add(user)
            return Response({'message':'User assigned to manager'},
                            status=status.HTTP_201_CREATED)
        elif request.method == 'DELETE':
            managers.user_set.remove(user)
        return Response({'message':'User removed'}, status=status.HTTP_200_OK)
    return Response({'message':'error'}, status=status.HTTP_404_NOT_FOUND)
