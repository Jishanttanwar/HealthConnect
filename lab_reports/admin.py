from django.contrib import admin

# Register your models here.

from .models import LabReport


@admin.register(LabReport)
class LabReportAdmin(admin.ModelAdmin):

    list_display = (
        "report_name",
        "status",
        "report_date",
        "encounter",
    )

    list_filter = (
        "status",
        "report_date",
    )

    search_fields = (
        "report_name",
        "encounter__appointment__patient__user__email",
        "encounter__appointment__doctor__user__email",
    )