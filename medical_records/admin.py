from django.contrib import admin

# Register your models here.

from .models import MedicalRecord
@admin.register(MedicalRecord)
class MedicalRecordAdmin(admin.ModelAdmin):

    list_display = (
        "patient",
        "status",
        "created_at",
    )

    list_filter = (
        "status",
    )

    search_fields = (
        "patient__user__email",
        "diagnosis",
    )