from django.db import models

from .items import Item
from .orders import Order
from .members import Member


class Cart(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.DO_NOTHING)
    quantity = models.PositiveIntegerField()
