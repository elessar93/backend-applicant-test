from rest_framework.permissions import BasePermission


class BlogPermission(BasePermission):
    def has_permission(self, request, view):
        if view.action == 'list':
            return True
        elif view.action == 'create':
            return request.user.is_staff
        elif view.action in ['retrieve', 'update', 'partial_update', 'destroy']:
            return True
        else:
            return False

    def has_object_permission(self, request, view, obj):
        # Deny actions on objects if the user is not authenticated
        if not request.user.is_authenticated:
            return False
        elif view.action in ['update', 'partial_update']:
            return obj.related_user == request.user or request.user.is_admin
        elif view.action == 'destroy':
            return request.user.is_superuser
        else:
            return False


class CommentPermission(BasePermission):
    def has_permission(self, request, view):
        if view.action == 'list':
            return True
        elif view.action == 'create':
            return request.user.is_authenticated
        elif view.action in ['retrieve', 'update', 'partial_update', 'destroy']:
            return True
        else:
            return False

    def has_object_permission(self, request, view, obj):
        # Deny actions on objects if the user is not authenticated
        if not request.user.is_authenticated:
            return False
        elif view.action in ['update', 'partial_update']:
            return obj.related_user == request.user or request.user.is_superuser
        elif view.action == 'destroy':
            return obj.related_user == request.user or request.user.is_superuser
        else:
            return False
