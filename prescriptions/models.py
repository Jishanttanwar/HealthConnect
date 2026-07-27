from django.db import models

# Create your models here.
#I am creating two models here. Because, if i store everything in one model, it will be difficult to manage the data. So, I am creating two models. One for Prescription and another for PrescriptionItem. Because, one prescription can have multiple items. So, I am creating a one-to-many relationship between Prescription and PrescriptionItem.
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



class PrescriptionItem(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    prescription = models.ForeignKey(
        Prescription,
        on_delete=models.CASCADE,
        related_name="items",
    )

    medicine_name = models.CharField(max_length=255)
    dosage = models.CharField(max_length=100)
    frequency = models.CharField(max_length=100)
    duration = models.CharField(max_length=100)
    instructions = models.TextField(blank=True)

    def __str__(self):
        return self.medicine_name