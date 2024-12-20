from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from .forms import CustomUserCreationForm, CustomUserChangeForm

class CustomUserAdmin(UserAdmin):
    """
    Custom admin panel for managing users.
    """
    add_form = CustomUserCreationForm  # Use custom creation form
    form = CustomUserChangeForm  # Use custom change form
    ordering = ['phone_number']

    model = User  # Use custom user model
    list_display = ('phone_number', 'first_name', 'last_name', 'is_staff', 'is_active')  # Fields to display in the admin list
    list_filter = ('is_staff', 'is_active')  # Filters for the admin list
    fieldsets = (  # Define the sections for user information
        (None, {'fields': ('phone_number', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (  # Fields to display in the add user form
        (None, {
            'classes': ('wide',),
            'fields': ('phone_number', 'password1', 'password2', 'is_staff', 'is_active'),
        }),
    )

admin.site.register(User, CustomUserAdmin)  # Register the custom user model with the admin panel
