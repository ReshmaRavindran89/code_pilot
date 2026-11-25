from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):

    def has_object_permission(self, request, view, obj):
        return request.user == obj.student

    

class IsAdmin(BasePermission):

    def has_object_permission(self, request, view, obj):
        return request.user == obj.assessment.creator


