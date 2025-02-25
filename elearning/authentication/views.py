from .models import *
from .serializers import *
from rest_framework import status
from django.contrib.auth import login
from django.core.mail import send_mail
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework_simplejwt.authentication import JWTAuthentication


class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            send_mail(
                "Your OTP Code",
                f"Your OTP for email verification is {user.otp}",
                "noreply@elearning.com",
                [user.email],
                fail_silently=False
            )
            return Response({"message": "User registered. Check your email for OTP"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class VerifyOTPView(APIView):
    def post(self, request):
        serializer = OTPVerificationSerializer(data=request.data)
        if serializer.is_valid():
            return Response({"message": "Email verified successfully"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data
            refresh = RefreshToken.for_user(user)  # Generate tokens
            return Response({
                # user details print 
                "user":{
                    "id": user.id,
                    "email": user.email,
                    "full_name": user.full_name,
                },
              
                "access": str(refresh.access_token),  # Access Token
                "refresh": str(refresh)  # Refresh Token
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]
    parser_classes = (MultiPartParser, FormParser)  
    def get(self, request, userId):
        user = get_object_or_404(CustomUser, id=userId)
        serializer = UserProfileSerializer(user)
        return Response(serializer.data)
    def put(self, request, userId):
        user = get_object_or_404(CustomUser, id=userId)
        serializer = UserProfileSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)
