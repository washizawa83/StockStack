import django_filters.rest_framework
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.response import Response

from api.models import Member
from api.serializers import MemberSerializer
from api.filters import MemberFilter


class MemberSearchView(generics.ListAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_class = MemberFilter


class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

