from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.core.exceptions import PermissionDenied
from ..serializers.kit import KitSerializer
from ..models.kit import Kit

class KitsView(APIView):
    def post(self, request):
        # Add the user id as owner
        request.data['owner'] = request.user.id
        kit = KitSerializer(data=request.data)
        if not kit.is_valid():
            return Response(kit.errors, status=status.HTTP_400_BAD_REQUEST)
        kit.save()
        return Response(kit.data, status=status.HTTP_201_CREATED)  

    def get(self, request):
        # filter for kits with our user id
        kits = Kit.objects.filter(owner=request.user.id)
        data = KitSerializer(kits, many=True).data
        return Response(data)



class KitView(APIView):
    def delete(self, request, pk):
        kit = get_object_or_404(Kit, pk=pk)
        # Check the kit's owner against the user making this request
        if request.user != kit.owner:
            raise PermissionDenied('Unauthorized, you do not own this kit')
        kit.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def get(self, request, pk):
        kit = get_object_or_404(Kit, pk=pk)
        if request.user != kit.owner:
            raise PermissionDenied('Unauthorized, you do not own this kit')
        data = KitSerializer(kit).data
        return Response(data)
    
    def patch(self, request, pk):
        kit = get_object_or_404(Kit, pk=pk)
        # Check the kit's owner against the user making this request
        if request.user != kit.owner:
            raise PermissionDenied('Unauthorized, you do not own this kit')
        # Ensure the owner field is set to the current user's ID
        request.data['owner'] = request.user.id
        updated_kit = KitSerializer(kit, data=request.data, partial=True)
        if updated_kit.is_valid():
            updated_kit.save()
            return Response(updated_kit.data)
        return Response(updated_kit.errors, status=status.HTTP_400_BAD_REQUEST)