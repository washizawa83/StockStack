from django.contrib import admin
from .models import Item, Member, MemberGroup, Tag, Order, Cart


admin.site.register(Item)
admin.site.register(Tag)
admin.site.register(Member)
admin.site.register(MemberGroup)
admin.site.register(Order)
admin.site.register(Cart)
