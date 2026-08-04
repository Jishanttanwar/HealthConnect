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
    

class WeekDay(models.TextChoices):
    MONDAY = "MONDAY", "Monday"
    TUESDAY = "TUESDAY", "Tuesday"
    WEDNESDAY = "WEDNESDAY", "Wednesday"
    THURSDAY = "THURSDAY", "Thursday"
    FRIDAY = "FRIDAY", "Friday"
    SATURDAY = "SATURDAY", "Saturday"
    SUNDAY = "SUNDAY", "Sunday"


class DoctorAvailability(models.Model):

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    doctor = models.ForeignKey(
        DoctorProfile,
        on_delete=models.CASCADE,
        related_name="availability"
    )

    day_of_week = models.CharField(
        max_length=20,
        choices=WeekDay.choices
    )

    start_time = models.TimeField()

    end_time = models.TimeField()

    is_available = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = [
            "day_of_week",
            "start_time",
        ]

        constraints = [
            models.UniqueConstraint(
                fields=["doctor", "day_of_week", "start_time"],
                name="unique_doctor_day_time"
            )
        ]

    def __str__(self):
        return (
            f"{self.doctor.user.username} "
            f"{self.day_of_week} "
            f"{self.start_time}"
        )


