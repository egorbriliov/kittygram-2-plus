"""Отображения для взаимодейтсвия с котиками."""
from rest_framework import viewsets, filters
from rest_framework.throttling import ScopedRateThrottle
from django_filters.rest_framework import DjangoFilterBackend

from .models import Achievement, Cat, User
from .permissions import OwnerOrReadOnly
from .trottling import WorkingHoursRateThrottle
# from .pagination import CatsPagination
from .serializers import AchievementSerializer, CatSerializer, UserSerializer


class CatViewSet(viewsets.ModelViewSet):
    """Отображение для данных о котиках."""

    queryset = Cat.objects.all()
    serializer_class = CatSerializer
    permission_classes = [OwnerOrReadOnly]

    throttle_classes = (WorkingHoursRateThrottle, ScopedRateThrottle)
    trottle_scope = 'low_request'

    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    pagination_class = None
    filterset_fields = ('color', 'birth_year')
    search_fields = ('name',)

    def perform_create(self, serializer):
        """Метод добавления котиков."""
        serializer.save(owner=self.request.user)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """Отображения для данных о пользователей."""

    queryset = User.objects.all()
    serializer_class = UserSerializer


class AchievementViewSet(viewsets.ModelViewSet):
    """Отображения для данных об ачивках заработанных котиками."""

    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer
