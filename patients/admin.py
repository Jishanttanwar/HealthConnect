from django.contrib import admin

from .models import PatientProfile

# Register your models here.

@admin.register(PatientProfile)
class PatientProfileAdmin(admin.ModelAdmin):
    list_display = ('user','blood_group','gender',)
    search_fields = ('user__email', 'emergency_contact_name',)
    
    