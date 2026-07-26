import uuid
from django.db import models
from appointments.models import Appointment


class Encounter(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    appointment = models.OneToOneField(
        Appointment,
        on_delete=models.CASCADE,
        related_name="encounter",
    )

    diagnosis = models.TextField()

    symptoms = models.TextField()

    treatment_plan = models.TextField(
        blank=True,
        null=True,
    )

    follow_up_date = models.DateField(
        blank=True,
        null=True,
    )

    notes = models.TextField(
        blank=True,
        null=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"Encounter - {self.appointment}"
