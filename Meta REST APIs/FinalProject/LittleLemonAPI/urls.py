from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('menu-items/', views.menu_items),
    path('api-token-auth/', obtain_auth_token),
    path('users/users/me', views.current_user),
    path('token/login', views.login),
    path('menu-items/<int:pk>', views.single_menu_item),
    path('groups/manager/users', views.groups_view)
]
