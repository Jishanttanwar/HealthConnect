from django.db import models

# Create your models here.
import uuid
from patients.models import PatientProfile

class MedicalRecord(models.Model):

    class RecordStatus(models.TextChoices):
        ACTIVE = "ACTIVE", "Active"
        CLOSED = "CLOSED", "Closed"

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    patient = models.ForeignKey(
        PatientProfile,
        on_delete=models.CASCADE,
        related_name="medical_records",
    )

    diagnosis = models.TextField()

    allergies = models.TextField(
        blank=True,
        null=True,
    )

    chronic_conditions = models.TextField(
        blank=True,
        null=True,
    )

    family_history = models.TextField(
        blank=True,
        null=True,
    )

    notes = models.TextField(
        blank=True,
        null=True,
    )

    status = models.CharField(
        max_length=20,
        choices=RecordStatus.choices,
        default=RecordStatus.ACTIVE,
    )

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.patient.user.username} Medical Record"