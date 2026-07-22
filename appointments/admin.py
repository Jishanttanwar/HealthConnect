from django.contrib import admin
from .models import Appointment
# Register your models here.

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):

    list_display = (
        "patient",
        "doctor",
        "appointment_date",
        "start_time",
        "status",
    )

    list_filter = (
        "status",
        "appointment_date",
    )

    search_fields = (
        "patient__user__email",
        "doctor__user__email",
    )

    ordering = (
        "appointment_date",
        "start_time",
    )