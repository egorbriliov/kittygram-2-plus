"""Пагинация для котиков."""
from rest_framework.pagination import PageNumberPagination


class CatsPagination(PageNumberPagination):
    """Пагинация для котиков."""

    page_size = 20
