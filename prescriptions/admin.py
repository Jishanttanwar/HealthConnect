from django.contrib import admin

# Register your models here.
from .models import Prescription, PrescriptionItem

class PrescriptionItemInline(admin.TabularInline):
    model = PrescriptionItem
    extra = 1

@admin.register(Prescription)
class PrescriptionAdmin(admin.ModelAdmin):
    list_display = ("id","encounter","created_at",)

    inlines = [PrescriptionItemInline]