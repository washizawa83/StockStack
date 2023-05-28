from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


class CustomUserAdmin(UserAdmin):
    list_display = ['username', 'email', 'is_active', 'is_admin', 'is_staff', 'is_manager']
    list_filter = ['is_active', 'is_admin', 'is_staff', 'is_manager']
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Permissions', {'fields': ('is_active', 'is_admin', 'is_staff', 'is_manager')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'is_active', 'is_admin', 'is_staff', 'is_manager'),
        }),
    )
    search_fields = ['username', 'email']
    ordering = ['username']


admin.site.register(User, CustomUserAdmin)
