from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'is_inventory_manager')
        extra_kwargs = {
            'password': {
                'write_only': True,
            }
        }
