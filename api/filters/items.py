import django_filters
from django.db import models

from api.models import Item


class ItemFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(method='custom_filter')

    class Meta:
        model = Item
        fields = ['name']

    def custom_filter(self, queryset, name, value):
        return queryset.filter(
            models.Q(name__icontains=value) |
            models.Q(tag__name__icontains=value)
        )
