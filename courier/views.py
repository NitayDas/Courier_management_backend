from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import *
from .serializers import PackageSerializer
from django.contrib.auth.models import User
from rest_framework.views import APIView



# for user registration
class RegisterUserView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        username = request.data.get("username")
        password = request.data.get("password")

        if not username or not password:
            return Response(
                {"error": "Username and password are required."},
                status=status.HTTP_400_BAD_REQUEST
            )

        if User.objects.filter(username=username).exists():
            return Response(
                {"error": "Username already exists."},
                status=status.HTTP_400_BAD_REQUEST
            )

        user = User.objects.create_user(username=username, password=password)
    
    
    
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