from django.contrib import admin

from .models import DoctorProfile

# Register your models here.
@admin.register(DoctorProfile)
class DoctorProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'department', 'specialization', 'consultation_fee')
    search_fields = ('user__email', 'license_number')
    list_filter = ('department', 'specialization')


