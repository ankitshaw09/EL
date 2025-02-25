from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
import random

class CustomUserManager(BaseUserManager):
    def create_user(self, email, full_name, password=None):
        if not email:
            raise ValueError("Users must have an email address")
        email = self.normalize_email(email)
        user = self.model(email=email, full_name=full_name)
        user.set_password(password)
        user.generate_otp()
        user.save(using=self._db)
        return user

    def create_superuser(self, email, full_name, password):
        user = self.create_user(email, full_name, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

    def get_by_natural_key(self, email):
        """Fix for authentication error"""
        return self.get(email=email)  # Ensure email lookup works

class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = None
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=255)
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)
    professional_headline = models.CharField(max_length=255, null=True, blank=True)

    # Educational Background
    current_role = models.CharField(max_length=255, null=True, blank=True)
    institution_name = models.CharField(max_length=255, null=True, blank=True)

    # Skills
    skills = models.TextField(null=True, blank=True)

    # Contact Information
    phone_number = models.CharField(max_length=20, null=True, blank=True)

    # Social Media Links
    linkedin_url = models.URLField(null=True, blank=True)
    github_url = models.URLField(null=True, blank=True)

    # Preferences
    language = models.CharField(max_length=50, default="English")
    notifications = models.BooleanField(default=True)
    timezone = models.CharField(max_length=50, default="IST")

    is_verified = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = CustomUserManager()  # Add this to use the manager

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["full_name"]

    def __str__(self):
        return self.email

    def generate_otp(self):
        self.otp = str(random.randint(1000, 9999))
        self.save()
