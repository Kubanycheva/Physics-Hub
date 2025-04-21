from rest_framework.permissions import BasePermission


class HasPermission(BasePermission):
    def has_permission(self, request, view):
        required_perm = getattr(view, 'required_permission', None)
        return required_perm is None or request.user.has_perm(required_perm)
