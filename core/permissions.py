from rest_framework.permissions import BasePermission


class IsAdmin(BasePermission):
    """
    Allows access only to ADMIN users.
    """

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.role == "ADMIN"
        )


class IsDoctor(BasePermission):
    """
    Allows access only to DOCTOR users.
    """

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.role == "DOCTOR"
        )


class IsPatient(BasePermission):
    """
    Allows access only to PATIENT users.
    """

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.role == "PATIENT"
        )


class IsAdminOrReadOnly(BasePermission):
    """
    Admins can perform all operations.
    Other authenticated users can only read.
    """

    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False

        if request.method in ("GET", "HEAD", "OPTIONS"):
            return True

        return request.user.role == "ADMIN"