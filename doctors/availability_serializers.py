from rest_framework import serializers
from .models import DoctorAvailability

class DoctorAvailabilitySerializer(serializers.ModelSerializer):

    class Meta:
        model = DoctorAvailability
        fields = "__all__"

    def validate(self, attrs):
        if attrs["end_time"] <= attrs["start_time"]:
            raise serializers.ValidationError(
                "End time must be after start time."
            )

        return attrs