
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from courier.views import RegisterUserView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('courier.urls')),
    path('register/', RegisterUserView.as_view(), name='register'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api-auth/', include('rest_framework.urls')),
   
]

