from rest_framework import serializers
from .models import Encounter

class EncounterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Encounter
        fields = "__all__"

    def validate_appointment(self, appointment):
        if appointment.status != "COMPLETED":
            raise serializers.ValidationError(
                "Encounter can only be created for completed appointments."
            )

        return appointment