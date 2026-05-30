"""Троттлы для ограничения количества запросов."""

import datetime

from rest_framework import throttling


class WorkingHoursRateThrottle(throttling.BaseThrottle):
    """Троттл для ограничения запросов в определенные часы."""

    def allow_request(self, request, view):
        """Разрешает запросы только в определенные часы."""
        now = datetime.datetime.now().hour
        if now >= 3 and now < 5:
            return False
        return True
