from .views import *
from django.urls import path

urlpatterns = [
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('auth/verify-otp/', VerifyOTPView.as_view(), name='verify-otp'),
    path('auth/login/', LoginView.as_view(), name='login'),
    
    path('user/profile/<int:userId>/', UserProfileView.as_view(), name='user_profile'),
]
