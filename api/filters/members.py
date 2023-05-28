import django_filters
from api.models import Member


class MemberFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Member
        fields = ['name']
