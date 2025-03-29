from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, permissions, status, generics
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from .models import Category, MenuItem, Cart, Order, OrderItem
from .serializers import MenuItemSerializer, UserSerializer, CartSerializer, OrderSerializer, OrderItemSerializer
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User, Group
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from .permissions import ManagerPermissions, DeliveryCrewPermissions
from decimal import Decimal
from datetime import date
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
def menu_items(request):
    if request.method == 'GET':
        items = MenuItem.objects.all()
        serialized_item = MenuItemSerializer(items, many=True)
        return Response(serialized_item.data)

    if not request.user.groups.filter(name='Manager').exists():
        return Response({'message':'You are not authorized'},
                        status=status.HTTP_403_FORBIDDEN)

    permission_classes([IsAuthenticated])
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

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated, ManagerPermissions])
def managers(request):
    if request.method == 'GET':
        users = User.objects.filter(groups__name='Manager').values('username', 'id')
        return Response(users, status=status.HTTP_200_OK)

    username = request.data['username']
    if username:
        user = get_object_or_404(User, username=username)
        managers = Group.objects.get(name="Manager")
        if request.method == 'POST':
            managers.user_set.add(user)
            return Response({'message':f'User {user.username} assigned to manager'},
                            status=status.HTTP_201_CREATED)

    return Response({'message':'error'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated, ManagerPermissions])
def remove_manager(request, pk):
    user = User.objects.get(pk=pk)
    manager_group = Group.objects.get(name='Manager')
    if user in manager_group.user_set.all():
        manager_group.user_set.remove(user)
        return Response({'message': f'User {user.username} removed!'}, status=status.HTTP_200_OK)

    return Response({'message':'error'}, status=status.HTTP_404_NOT_FOUND)

class UserList(generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [permissions.IsAuthenticated, ManagerPermissions]

class DeliveryCrewList(generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [permissions.IsAuthenticated , ManagerPermissions]

    def get_queryset(self):
        return User.objects.filter(groups__name='Delivery crew')

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        if not username:
            return Response({'message':'Username is required'})

        user = User.objects.get(username=username)
        delivery_crew_group = Group.objects.get(name="Delivery crew")
        delivery_crew_group.user_set.add(user)
        return Response({'message': f'User {user.username} added to Delivery crew'},
                        status=status.HTTP_201_CREATED)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated, ManagerPermissions])
def remove_delivery_crew(request, pk):
    user = User.objects.get(pk=pk)
    delivery_group = Group.objects.get(name='Delivery crew')

    if user in delivery_group.user_set.all():
        delivery_group.user_set.remove(user)
        return Response({'message': f'User {user.username} removed!'}, status=status.HTTP_200_OK)
    else:
        return Response({'message':'error'}, status=status.HTTP_404_NOT_FOUND)


class CartViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request):
        """GET /api/cart/menu-items - List cart items"""
        carts = Cart.objects.filter(user=request.user)
        serialized_items = CartSerializer(carts, many=True)
        return Response(serialized_items.data)

    def create(self, request, *args, **kwargs):
        """POST /api/cart/menu-items - Add item to cart"""
        menuitem_id = request.data.get('menuitem_id')
        quantity = int(request.data.get('quantity', 1))

        if not menuitem_id:
            return Response(
                {'message': 'menuitem_id is required'},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            menuitem = MenuItem.objects.get(pk=menuitem_id)
        except MenuItem.DoesNotExist:
            return Response(
                {'message': 'Menu item not found'},
                status=status.HTTP_404_NOT_FOUND
            )

        # Calculate prices
        unit_price = menuitem.price
        price = unit_price * quantity

        # Create or update cart item
        cart_item, created = Cart.objects.get_or_create(
            user=request.user,
            menuitem=menuitem,
            defaults={
                'quantity': quantity,
                'unit_price': unit_price,
                'price': price
            }
        )

        if not created:
            cart_item.quantity += quantity
            cart_item.price = cart_item.quantity * cart_item.unit_price
            cart_item.save()

        return Response(
            {'message': f'{menuitem.title} added to cart'},
            status=status.HTTP_201_CREATED
        )

    def destroy(self, request):
        """DELETE /api/cart/menu-items - Clear entire cart"""
        deleted_count, _ = Cart.objects.filter(user=request.user).delete()
        return Response(
            {'message': f'Cart cleared ({deleted_count} items removed)'},
            status=status.HTTP_200_OK
        )

# Orders

class OrdersViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request):

        if ManagerPermissions().has_permission(request, self):
            queryset = Order.objects.all()
            print('manager returned')
        else:
            queryset = Order.objects.filter(user=request.user)
            print('else returned')

        serializer_class = OrderItemSerializer(queryset, many = True)
        return Response(serializer_class.data)

    def create(self, request):
        pass
