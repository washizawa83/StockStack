import django_filters.rest_framework
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.response import Response

from api.models import MemberGroup
from api.serializers import GroupSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = MemberGroup.objects.all()
    serializer_class = GroupSerializer
