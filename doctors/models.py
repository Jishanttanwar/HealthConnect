import uuid
from django.db import models
from accounts.models import User
from departments.models import Department
from specializations.models import Specialization
# Create your models here.
class WeekDay(models.TextChoices):
    MONDAY = "MONDAY", "Monday"
    TUESDAY = "TUESDAY", "Tuesday"
    WEDNESDAY = "WEDNESDAY", "Wednesday"
    THURSDAY = "THURSDAY", "Thursday"
    FRIDAY = "FRIDAY", "Friday"
    SATURDAY = "SATURDAY", "Saturday"
    SUNDAY = "SUNDAY", "Sunday"
class DoctorAvailability(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)

    doctor = models.ForeignKey("DoctorProfile",on_delete=models.CASCADE,related_name="availability")
    day_of_week = models.CharField(max_length=20,choices=WeekDay.choices)
    start_time = models.TimeField()
    end_time = models.TimeField()
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
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




