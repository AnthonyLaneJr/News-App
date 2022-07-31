from django.contrib import admin

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserChangeForm, CustomUserCreationForm, CustomUserCreationForm
from .models import CustomUser, Department


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        (None, {"fields": ("role", "department")}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {"fields": ("role", "department")}),
    )
    list_display = [
        "username", "email", "first_name", "last_name",
        "role", "department", "is_staff",
        ]


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Department)