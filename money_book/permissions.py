from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # If HTTP Method is SAFE_METHOD(GET) - True
        if request.method in permissions.SAFE_METHODS:
            return True
        # Owner Validation
        return obj.author == request.user
