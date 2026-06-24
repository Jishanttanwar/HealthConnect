from rest_framework import serializers
from .models import DoctorProfile

class DoctorProfileSerializer(serializers.ModelSerializer):
    department_name = serializers.CharField(source='department.name', read_only=True)
    specialization_name = serializers.CharField(source='specialization.name', read_only=True)
    doctor_name = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = DoctorProfile
        fields = '__all__'

