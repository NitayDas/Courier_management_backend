from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import PackageSerializer

class PackageViewSet(viewsets.ModelViewSet):
    queryset = Package.objects.filter(is_deleted=False)
    serializer_class = PackageSerializer
    # permission_classes = [IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        package = self.get_object()
        package.is_deleted = True  # Mark as deleted instead of removing from DB
        package.save()
        return Response({'message': 'Package is softly deleted'}, status=status.HTTP_204_NO_CONTENT)
