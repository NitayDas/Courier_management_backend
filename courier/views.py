from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import *
from .serializers import PackageSerializer



class PackageViewSet(viewsets.ModelViewSet):
    queryset = Package.objects.filter(is_deleted=False)
    serializer_class = PackageSerializer

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:  # Require authentication for update & delete
            return [IsAuthenticated()]
        return [AllowAny()]  
    
    
    def destroy(self, request, *args, **kwargs):
        package = self.get_object()
        package.is_deleted = True  # Mark as deleted instaed of permanent delete
        package.save()
        return Response({'message': 'Package is softly deleted'}, status=status.HTTP_204_NO_CONTENT)