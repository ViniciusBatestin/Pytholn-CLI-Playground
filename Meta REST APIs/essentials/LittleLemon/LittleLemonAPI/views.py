from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, throttle_classes
from .models import MenuItem
from .serializers import MenuItemSerializer
from django.shortcuts import get_object_or_404
from rest_framework import status
from django.core.paginator import Paginator,EmptyPage
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from .throttles import TenCallsPerMinute
# admin
from rest_framework.permissions import IsAdminUser
from django.contrib.auth.models import User, Group
# Create your views here.

@api_view(['GET', "POST"])
def menu_items(request):
    if request.method == 'GET':
        items = MenuItem.objects.select_related('category').all()
        category_name = request.query_params.get('category')
        to_price = request.query_params.get('to_price')
        search = request.query_params.get('search')
        ordering = request.query_params.get('ordering')
        perpage = request.query_params.get('perpage', default=2)
        page = request.query_params.get('page', default = 1)
        if category_name:
            items = items.filter(category__title=category_name)
        if to_price:
            items = items.filter(price__lte=to_price)
        if search:
            items = items.filter(title__contains=search)
        if ordering:
            ordering_fields = ordering.split(",")
            items = items.order_by(*ordering_fields)

        #Paginator
        paginator = Paginator(items, per_page = perpage)
        try:
            items = paginator.page(number=page)
        except EmptyPage:
            items = []

        serialized_item = MenuItemSerializer(items, many=True)
        return Response(serialized_item.data)

    if request.method == 'POST':
        serialized_item = MenuItemSerializer(data=request.data)
        serialized_item.is_valid(raise_exception=True)
        serialized_item.save()
        return Response(serialized_item.data, status.HTTP_201_CREATED)



@api_view()
def single_view(request, id):
    item = get_object_or_404(MenuItem, pk=id)
    serialized_item = MenuItemSerializer(item)#Many = true not required for single options
    return Response(serialized_item.data)

@api_view()
@permission_classes([IsAuthenticated])
def secret(request):
    return Response({"message":"Some secret message"})

@api_view()
@permission_classes([IsAuthenticated])
def manager_view(request):
    if request.user.groups.filter(name='Manager').exists():
        return Response({"message":"Only managers see this"})
    else:
        return Response({"message": "You are not authorized"}, 403)

@api_view()
@throttle_classes([AnonRateThrottle])
def throttle_check(request):
    return Response({"message":"successful"})

@api_view()
@permission_classes([IsAuthenticated])
@throttle_classes([TenCallsPerMinute]) #I can specify individually how much, can a user call particular endpoint.
def throttle_check_auth(request):
    return Response({"message":"Message for the logged in users"})

# Supper admin can add and remove users from groups
@api_view(['POST'])
@permission_classes([IsAdminUser])
def managers(request):
    username = request.data['username']
    if username:
        user = get_object_or_404(User, username=username)
        managers = Group.objects.get(name="Manager")
        if request.method == 'POST':
            managers.user_set.add(user)
        elif request.method == 'DELETE':
            managers.user_set.remove(user)
        return Response({"message":"OK"})

    return Response({"message":"error"}, status.HTTP_400_BAD_REQUEST)
