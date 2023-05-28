from rest_framework import serializers
from api.models import MemberGroup


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = MemberGroup
        fields = '__all__'

