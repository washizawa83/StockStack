from rest_framework import generics

from api.models import Order
from api.serializers import OrderSerializer


class OrderListView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

