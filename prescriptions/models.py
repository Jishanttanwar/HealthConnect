from django.db import models

# Create your models here.
import uuid
from encounters.models import Encounter
class Prescription(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    encounter = models.OneToOneField(
        Encounter,
        on_delete=models.CASCADE,
        related_name="prescription",
    )
    notes = models.TextField(
        blank=True,
        null=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"Prescription {self.id}"