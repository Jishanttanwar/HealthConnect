from django.contrib import admin

# Register your models here.
from .models import Encounter
@admin.register(Encounter)
class EncounterAdmin(admin.ModelAdmin):
    list_display = (
        "appointment",
        "follow_up_date",
        "created_at",
    )

    search_fields = (
        "appointment__patient__user__email",
        "appointment__doctor__user__email",
    )

    ordering = (
        "-created_at",
    )
