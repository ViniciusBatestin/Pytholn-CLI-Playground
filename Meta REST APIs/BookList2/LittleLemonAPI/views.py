from rest_framework import generics
from .models import MenuItem
from .serializer import MenuItemSerializer

# Create your views here.

class MenuItemsViews(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
