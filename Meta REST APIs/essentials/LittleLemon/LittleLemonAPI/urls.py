from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('menu-items/', views.menu_items),
    path('menu-items/<int:id>', views.single_view),
    path('secret/', views.secret),
    path('api-token-auth/', obtain_auth_token),
    path('manager-view/', views.manager_view),
    path('throttle-check', views.throttle_check),
    path('throttle-check-auth', views.throttle_check_auth),
]


# "token": "9e0a45a75066c135d02329417c28beeec4d7a687" mapekinha
# "token": "a9bb24a7423351f2d76389d30a62563a71d6f623" Marshmellow
