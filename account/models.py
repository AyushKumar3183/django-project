from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager

# Custom User Manager
class UserManager(BaseUserManager):
    def create_user(self, phone_number, password=None, **extra_fields):
        if not phone_number:
            raise ValueError("Phone number is required")
        extra_fields['email'] = self.normalize_email(extra_fields.get('email'))
        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(phone_number, password, **extra_fields)

# Custom User Model
class CustomUser(AbstractUser):
    username = None  # Remove the username field
    phone_number = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    user_bio = models.CharField(max_length=50)
    user_profile = models.ImageField(upload_to='profile/')

    USERNAME_FIELD = 'phone_number'  # Set phone_number as the unique identifier
    REQUIRED_FIELDS = ['email']  # Specify required fields for createsuperuser

    # Assign the custom user manager
    objects = UserManager()

    def __str__(self):
        return self.phone_number  # String representation of the user
