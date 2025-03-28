from rest_framework import permissions

class ManagerPermissions(permissions.BasePermission):
    edit_methods = ('PUT', 'PATCH')
    def has_permission(self, request, view):
        return request.user.groups.filter(name='Manager').exists()

class DeliveryCrewPermissions(permissions.BasePermission):
    edit_methods = ('PUT', 'PATCH')
    def has_permission(self, request, view):
        return request.user.groups.filter(name='Delivery crew').exists()
