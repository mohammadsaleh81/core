from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models


class CustomUserManager(BaseUserManager):
    def create_user(self, phone_number, password=None, **extra_fields):
        """
        Create a regular user with the given phone number and password.
        """
        if not phone_number:
            raise ValueError('The phone number is required')
        phone_number = self.normalize_email(phone_number)  # Normalize the phone number if necessary
        extra_fields.setdefault('is_active', True)  # Default to active
        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_password(password)  # Set the user password
        user.save(using=self._db)  # Save the user in the database
        return user

    def create_superuser(self, phone_number, password=None, **extra_fields):
        """
        Create a superuser with the given phone number and password.
        """
        extra_fields.setdefault('is_staff', True)  # Superuser must be staff
        extra_fields.setdefault('is_superuser', True)  # Superuser must have all permissions

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(phone_number, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    phone_number = models.CharField(max_length=15, unique=True)  # Unique phone number for user identification
    first_name = models.CharField(max_length=30, blank=True)  # First name (optional)
    last_name = models.CharField(max_length=30, blank=True)  # Last name (optional)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True, null=True)

    objects = CustomUserManager()  # Custom manager for handling user creation

    USERNAME_FIELD = 'phone_number'  # Phone number will be used as the username field
    REQUIRED_FIELDS = []  # No additional required fields for creating a superuser

    def __str__(self):
        return self.phone_number  # Display the phone number as the string representation
