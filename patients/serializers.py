from rest_framework import serializers
from .models import PatientProfile


class PatientProfileSerializer(serializers.ModelSerializer):
    patient_name = serializers.CharField(source='user.username', read_only=True)
    patient_email = serializers.EmailField(source='user.email', read_only=True)

    class Meta:
        model = PatientProfile
        fields = '__all__'



     

    


















