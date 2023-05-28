from rest_framework import viewsets
from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response

from api.models import Cart, Order, Member, Item
from api.serializers import CartSerializer


class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    def create(self, request, *args, **kwargs):
        order, created = Order.objects.get_or_create(is_ordered=False, user_id=request.user.id)
        item = Item.objects.get(pk=request.data.get('item_id'))
        member = Member.objects.get(pk=request.data.get('member_id'))
        item = item
        member = member
        quantity = request.data.get('quantity')
        cart = Cart.objects.create(item=item, order=order, member=member, quantity=quantity)

        serializer = self.get_serializer(cart)
        response = serializer.data

        return Response(response, status=status.HTTP_201_CREATED)


class OrderInCartView(generics.ListAPIView):
    serializer_class = CartSerializer

    def get_queryset(self):
        order_id = self.kwargs['order_id']
        return Cart.objects.filter(order_id=order_id)


class MemberCartView(generics.ListAPIView):
    serializer_class = CartSerializer

    def get_queryset(self):
        order = Order.objects.filter(is_ordered=False).first()
        member_id = self.kwargs['member_id']
        return Cart.objects.filter(order_id=order.id, member_id=member_id)
