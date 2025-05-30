from rest_framework.permissions import BasePermission
from django.utils.translation import gettext_lazy as _

from users.models import UserRoles


class IsModerator(BasePermission):
    """
    Разрешение для проверки роли модератора.
    Позволяет доступ только пользователям с ролью модератора.
    Если пользователь не является модератором, возвращает сообщение об ошибке.
    """
    message = _('You are not a moderator')

    def has_permission(self, request, view):
        if request.user.role == UserRoles.MODERATOR:
            return True
        else:
            return False


class IsSuperuser(BasePermission):
    """
    Разрешение для проверки суперпользователя.
    Позволяет доступ только пользователям, которые являются суперпользователями.
    Если пользователь не является суперпользователем, возвращает сообщение об ошибке.
    """
    message = _('You are not a superuser')

    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        return False
