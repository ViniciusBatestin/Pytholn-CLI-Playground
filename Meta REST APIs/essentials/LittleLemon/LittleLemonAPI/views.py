from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import MenuItem
from .serializers import MenuItemSerializer
from django.shortcuts import get_object_or_404
# Create your views here.

@api_view(['GET', "POST"])
def menu_items(request):
    items = MenuItem.objects.select_related('category').all()
    serialized_item = MenuItemSerializer(items, many=True)
    return Response(serialized_item.data)

@api_view()
def single_view(request, id):
    item = get_object_or_404(MenuItem, pk=id)
    serialized_item = MenuItemSerializer(item)#Many = true not required for single options
    return Response(serialized_item.data)
