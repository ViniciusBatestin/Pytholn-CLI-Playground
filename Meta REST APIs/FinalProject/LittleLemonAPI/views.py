from django.shortcuts import render
from rest_framework import status, generics, viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from .models import Category, MenuItem, Cart, Order, OrderItem
from .serializers import MenuItemSerializer
#Auth imports
from rest_framework.permissions import IsAuthenticated



# Create your views here.
@api_view(['GET', 'POST'])
def menu_items(request):
    items = MenuItem.objects.all()
    serialized_item = MenuItemSerializer(items, many=True)
    return Response(serialized_item.data)



# if request.user.groups.filter(name='Manager').exists():
#     return
