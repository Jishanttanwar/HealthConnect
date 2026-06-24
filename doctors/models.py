import uuid
from django.db import models
from accounts.models import User
from departments.models import Department
from specializations.models import Specialization
# Create your models here.


class DoctorProfile(models.Model):
    id = models.UUIDField(primary_key=True, default= uuid.uuid4, editable= False)
    user = models.OneToOneField(User, on_delete= models.CASCADE, related_name= 'doctor_profile')
    department = models.ForeignKey(Department, on_delete= models.PROTECT, related_name = 'doctors')
    specialization = models.ForeignKey(Specialization, on_delete= models.PROTECT , related_name = 'doctors')

    qualification = models.CharField(max_length= 255)
    experience_years = models.PositiveIntegerField(default= 0)
    license_number = models.CharField(max_length=100, unique=True)
    consultation_fee = models.DecimalField(max_digits=10, decimal_places=2)
    bio = models.TextField(blank=True, null=True )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Dr. {self.user.username}"




