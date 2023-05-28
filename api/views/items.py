import django_filters.rest_framework
from rest_framework import generics
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response

from api.models import Item, Tag
from api.serializers import ItemSerializer, TagSerializer
from api.filters import ItemFilter


def create_or_delete_tags(item, tags):
    item.tag.clear()
    tags = tags.split()
    for tag in tags:
        tag = tag.lower()
        if not item.tag.filter(name=tag).exists():
            if Tag.objects.filter(name=tag).exists():
                add_tag = Tag.objects.filter(name=tag).first()
                item.tag.add(add_tag)
            else:
                add_tag = Tag.objects.create(name=tag)
                item.tag.add(add_tag)


class ItemSearchView(generics.ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_class = ItemFilter


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def create(self, request, *args, **kwargs):
        tags = request.data['tags']
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        item = serializer.instance

        if request.data['tags']:
            tags = request.data['tags'].split(' ')
            for tag in tags:
                if Tag.objects.filter(name=tag).exists():
                    add_tag = Tag.objects.filter(name=tag).first()
                    item.tag.add(add_tag)
                else:
                    add_tag = Tag.objects.create(name=tag)
                    item.tag.add(add_tag)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        if not request.user:
            serializer.validated_data['unit_price'] = instance.unit_price
        self.perform_update(serializer)
        if request.data['tags']:
            print(request.data['tags'])
            create_or_delete_tags(instance, request.data['tags'])
        return Response(serializer.data)


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

