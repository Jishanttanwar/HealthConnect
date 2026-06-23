
import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import UserManager


# Create your models here.

class UserRole(models.TextChoices):
    PATIENT = 'PATIENT', 'Patient'
    DOCTOR = 'DOCTOR', 'Doctor'
    RECEPTIONIST = 'RECEPTIONIST', 'Receptionist'
    ADMIN = 'ADMIN', 'Admin'

class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank = True , null = True)
    role = models.CharField(max_length=20, choices=UserRole.choices)
    is_verified = models.BooleanField(default = False)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now=True)
    

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()


    def __str__(self):
        return self.email
 





