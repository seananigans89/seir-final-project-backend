from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.core.exceptions import PermissionDenied
from ..serializers.item import ItemSerializer
from ..models.item import Item

class ItemsView(APIView):
    def post(self, request):
        # Add the user id as owner
        print(request.data)
        request.data['owner'] = request.user.id
        print(request.data)
        item = ItemSerializer(data=request.data)
        print(item)
        if not item.is_valid():
            print('4')  
            return Response(item.errors, status=status.HTTP_400_BAD_REQUEST)
        item.save()
        print('5')
        return Response(item.data, status=status.HTTP_201_CREATED)  

    def get(self, request):
        # filter for items with our user id
        items = Item.objects.filter(owner=request.user.id)
        data = ItemSerializer(items, many=True).data
        return Response(data)



class ItemView(APIView):
    def delete(self, request, pk):
        item = get_object_or_404(Item, pk=pk)
        # Check the item's owner against the user making this request
        if request.user != item.owner:
            raise PermissionDenied('Unauthorized, you do not own this item')
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def get(self, request, pk):
        item = get_object_or_404(Item, pk=pk)
        if request.user != item.owner:
            raise PermissionDenied('Unauthorized, you do not own this item')
        data = ItemSerializer(item).data
        return Response(data)
    
    def patch(self, request, pk):
        item = get_object_or_404(Item, pk=pk)
        # Check the item's owner against the user making this request
        if request.user != item.owner:
            raise PermissionDenied('Unauthorized, you do not own this item')
        # Ensure the owner field is set to the current user's ID
        request.data['owner'] = request.user.id
        updated_item = ItemSerializer(item, data=request.data, partial=True)
        if updated_item.is_valid():
            updated_item.save()
            return Response(updated_item.data)
        return Response(updated_item.errors, status=status.HTTP_400_BAD_REQUEST)