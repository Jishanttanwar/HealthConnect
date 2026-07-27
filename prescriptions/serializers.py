from rest_framework import serializers
from .models import Prescription, PrescriptionItem

class PrescriptionItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrescriptionItem
        fields = "__all__"

class PrescriptionSerializer(serializers.ModelSerializer):
    items = PrescriptionItemSerializer(many=True)

    class Meta:
        model = Prescription
        fields = "__all__"

    def validate_encounter(self, encounter):
        if hasattr(encounter, "prescription"):
            raise serializers.ValidationError(
                "This encounter already has a prescription."
            )
        return encounter

    def create(self, validated_data):
        items = validated_data.pop("items")

        prescription = Prescription.objects.create(**validated_data)

        for item in items:
            PrescriptionItem.objects.create(
                prescription=prescription,
                **item
            )

        return prescription