from rest_framework import serializers
from ..models.kit import Kit

class KitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kit
        fields = ('name', 'description', 'gearList', 'category', 'owner')



