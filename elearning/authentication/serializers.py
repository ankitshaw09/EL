from .models import CustomUser
from rest_framework import serializers
from django.contrib.auth import authenticate

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['full_name', 'email', 'password']

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            email=validated_data['email'],
            full_name=validated_data['full_name'],
            password=validated_data['password']
        )
        return user
    
class OTPVerificationSerializer(serializers.Serializer):
    email = serializers.EmailField()
    otp = serializers.CharField(max_length=4)

    def validate(self, data):
        try:
            user = CustomUser.objects.get(email=data['email'])
            if user.otp == data['otp']:
                user.is_verified = True
                user.otp = None
                user.save()
                return data
            else:
                raise serializers.ValidationError("Invalid OTP")
        except CustomUser.DoesNotExist:
            raise serializers.ValidationError("User not found")

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(username=data['email'], password=data['password'])
        if user is None:
            raise serializers.ValidationError("Invalid credentials")
        if not user.is_verified:
            raise serializers.ValidationError("Email not verified")
        return user

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            "id", "email", "full_name", "profile_photo", "professional_headline",
            "current_role", "institution_name", "skills", "phone_number",
            "linkedin_url", "github_url", "language", "notifications", "timezone"
        ]
