"""Модуль для прав взаимодействия с котиками."""

from rest_framework import permissions
from rest_framework.request import Request
from rest_framework.views import APIView


class OwnerOrReadOnly(permissions.BasePermission):
    """Класс который разрешает изменение для владелца и просмот для всех."""

    def has_permission(self,
                       request: Request,
                       view: APIView) -> bool:
        """Проверяет чтобы пользователь был авторизирован на уровне запроса."""
        return (
                request.method in permissions.SAFE_METHODS
                or request.user.is_authenticated
            )

    def has_object_permission(self,
                              request: Request,
                              view: APIView, obj) -> bool:
        """Проверяет, чтобы пользователь был владельцем."""
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request


class ReadOnly(permissions.BasePermission):
    """Разрешает анонимному пользователю выполнять чтение из БД."""

    def has_permission(self, request, view) -> bool:
        """Проверяет, чтобы был метод запроса."""
        return request.method in permissions.SAFE_METHODS
