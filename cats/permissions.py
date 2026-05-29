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

    def has_object_permission(self, request, view, obj) -> bool:
        """Проверяет, чтобы пользователь был владельцем."""
        return obj.owner == request.user


class ReadOnly(permissions.BasePermission):
    """Разрешает анонимному пользователю выполнять чтение из БД."""

    def has_permission(self, request, view) -> bool:
        """Проверяет, чтобы был метод запроса."""
        return request.method in permissions.SAFE_METHODS
