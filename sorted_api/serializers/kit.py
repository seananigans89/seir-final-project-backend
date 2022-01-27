from rest_framework import serializers

from sorted_api.models.item import Item
from ..models.kit import Kit
from ..models import User

class KitOwnerSerializer(serializers.ModelSerializer): 
    class Meta:
        model = User
        fields = ('id', 'email' )

class KitItemSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Item
        fields = ('id', 'brand', 'model', 'serial_number', 'quantity', 'category', 'owner')

class KitSerializer(serializers.ModelSerializer):

    owner = KitOwnerSerializer(required=False)
    # gearList = serializers.PrimaryKeyRelatedField(many = True, required = False, read_only=False, queryset = Item.objects.all())
    gearList = KitItemSerializer(many=True, required=False)
    class Meta:
        model = Kit
        fields = ('name', 'description', 'gearList', 'category', 'owner', 'id')
        depth = 1

class NewKitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kit
        fields = ('name', 'description', 'gearList', 'category', 'id' )


