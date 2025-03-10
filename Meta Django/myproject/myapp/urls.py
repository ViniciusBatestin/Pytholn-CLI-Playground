from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home),
    path('dishes/<str:dish>', views.menuitems),
    path('drinks/<str:drink_name>', views.drinks, name='drinks'),
]
