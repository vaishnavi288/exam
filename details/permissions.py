from rest_framework.permissions import BasePermission

class AuthenticatedORIS_Superuser(BasePermission):
    def has_permission(self, request, view):
        if request.method=='GET':
           return request.user.is_authenticated
        return request.user.is_superuser


    def has_object_permission(self, request, view, obj):
        if request.method=='GET':
            return request.user.is_authenticated
        return request.user.is_superuser