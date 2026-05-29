"""Модуль для прав взаимодействия с котиками."""

from rest_framework import permissions


class OwnerOrReadOnly(permissions.BasePermission):
    """Класс который разрешает изменение для владелца и просмот для всех."""

    def has_permission(self, request, view):
        """Проверяет чтобы пользователь был авторизирован на уровне запроса."""
        return (
                request.method in permissions.SAFE_METHODS
                or request.user.is_authenticated
            )

    def has_object_permission(self, request, view, obj):
        """Проверяет, чтобы пользователь был владельцем."""
        return obj.owner == request.user
