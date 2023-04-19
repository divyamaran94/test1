from rest_framework import permissions

class IsVaccinecenterOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # return super().has_object_permission(request, view, obj)
        return obj.created_by==request.user