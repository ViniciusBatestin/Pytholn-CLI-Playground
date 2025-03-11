from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('aboutus/', views.about, name='abaout'),
    path('menu/', views.menu, name="menu"),
    path('book/', views.book, name="book")
]


# urlpatterns = [
#     path('home/', views.home),
#     path('dishes/<str:dish>', views.menuitems),
#     path('drinks/<str:drink_name>', views.drinks, name='drinks'),
# ]
