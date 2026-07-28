from django.db import models

# Create your models here.
import uuid
from encounters.models import Encounter

class LabReport(models.Model):

    class ReportStatus(models.TextChoices):
        PENDING = "PENDING", "Pending"
        COMPLETED = "COMPLETED", "Completed"

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    encounter = models.ForeignKey(
        Encounter,
        on_delete=models.CASCADE,
        related_name="lab_reports",
    )

    report_name = models.CharField(max_length=255)

    report_date = models.DateField()

    result_summary = models.TextField()

    doctor_notes = models.TextField(
        blank=True,
        null=True,
    )

    report_file = models.FileField(
        upload_to="lab_reports/",
        blank=True,
        null=True,
    )

    status = models.CharField(
        max_length=20,
        choices=ReportStatus.choices,
        default=ReportStatus.PENDING,
    )

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-report_date"]

    def __str__(self):
        return self.report_name