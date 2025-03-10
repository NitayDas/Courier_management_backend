from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import *
from .serializers import *
from django.contrib.auth.models import User
from rest_framework.generics import CreateAPIView



# for user registration
class RegisterUserView(CreateAPIView):
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(
            {"message": "User registered successfully."},
            status=status.HTTP_201_CREATED
        )
        
    
    
# CRUD operation on Packages
class PackageViewSet(viewsets.ModelViewSet):
    queryset = Package.objects.filter(is_deleted=False)
    serializer_class = PackageSerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:  # Require authentication for update & delete
            return [IsAuthenticated()]
        return [AllowAny()]  
    
    
    def destroy(self, request, *args, **kwargs):
        package = self.get_object()
        package.is_deleted = True  # Mark as deleted instaed of permanent delete
        package.save()
        return Response({'message': 'Package is softly deleted'}, status=status.HTTP_204_NO_CONTENT)