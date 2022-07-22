from asyncio import exceptions
from rest_framework.permissions import BasePermission,SAFE_METHODS

class TwitterUserPermission(BasePermission):
    def has_object_permission(self, request, view,obj):
        message = "you dont have permission to make or delete tweet"
        if request.method in SAFE_METHODS:
            return True
        else:
            return obj.owner==request.user
