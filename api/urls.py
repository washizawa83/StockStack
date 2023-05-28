from django.urls import path, include
from . import views
from rest_framework import routers

defaultRouter = routers.DefaultRouter()
defaultRouter.register('items', views.ItemViewSet)
defaultRouter.register('members', views.MemberViewSet)
defaultRouter.register('groups', views.GroupViewSet)
defaultRouter.register('carts', views.CartViewSet)

urlpatterns = [
    path('items/search/', views.ItemSearchView.as_view(), name='items_search'),
    path('members/search/', views.MemberSearchView.as_view(), name='members_search'),
    path('orders/', views.OrderListView.as_view(), name="order_list"),
    path('carts/order/<int:order_id>/', views.OrderInCartView.as_view(), name='order_in_carts'),
    path('carts/member/<int:member_id>/', views.MemberCartView.as_view(), name="member_carts"),
    path('', include(defaultRouter.urls)),
]
