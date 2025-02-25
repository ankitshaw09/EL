from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ("email", "full_name", "is_verified", "is_staff", "is_active")
    list_filter = ("is_staff", "is_verified", "is_active")
    ordering = ("email",)
    search_fields = ("email", "full_name")

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Personal Info", {"fields": ("full_name", "profile_photo", "professional_headline")}),
        ("Education", {"fields": ("current_role", "institution_name")}),
        ("Skills", {"fields": ("skills",)}),
        ("Contact Info", {"fields": ("phone_number", "linkedin_url", "github_url")}),
        ("Preferences", {"fields": ("language", "notifications", "timezone")}),
        ("Permissions", {"fields": ("is_verified", "is_staff", "is_active", "groups", "user_permissions")}),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "full_name", "password1", "password2", "is_verified", "is_staff", "is_active"),
        }),
    )

    filter_horizontal = ("groups", "user_permissions")

admin.site.register(CustomUser, CustomUserAdmin)
