from rest_framework.permissions import SAFE_METHODS, BasePermission


class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return bool(
            request.user
            and request.user.is_authenticated
            and request.user.role in {"ADMIN", "SUPER_ADMIN"}
        )


class IsContactMessageUser(BasePermission):
    def has_permission(self, request, view):
        if request.method == "POST":
            return True
        return bool(
            request.user
            and request.user.is_authenticated
            and request.user.role in {"ADMIN", "SUPER_ADMIN"}
        )