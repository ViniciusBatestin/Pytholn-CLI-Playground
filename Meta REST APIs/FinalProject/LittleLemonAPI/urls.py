from django.urls import path, include
from . import views
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register(r'cart/menu-items', views.CartViewSet, basename='cart')

urlpatterns = [
    # path('', include(router.urls)),
    path('menu-items/', views.menu_items),
    path('menu-items/<int:pk>', views.single_menu_item),

    path('api-token-auth/', obtain_auth_token),
    path('users/users/me', views.current_user),
    path('token/login', views.login),

    path('groups/manager/users', views.managers),
    path('groups/manager/users/<int:pk>', views.remove_manager),
    path('groups/delivery-crew/users', views.DeliveryCrewList.as_view()),
    path('groups/delivery-crew/users/<int:pk>', views.remove_delivery_crew),

    path('cart/menu-items/', views.CartViewSet.as_view({
        'delete': 'destroy',
        'get': 'list',
        'post': 'create',
    })),

    path('orders/', views.OrdersViewSet.as_view({
        'get': 'list',
        'post': 'create',
        'put': 'retrieve',
        'patch': 'update',
        'delete': 'destroy',

        })),

    path('userlist', views.UserList.as_view())
]
