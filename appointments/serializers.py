from datetime import date

from rest_framework import serializers

from .models import Appointment


class AppointmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Appointment
        fields = "__all__"

    def validate(self, data):
        appointment_date = data["appointment_date"]
        start_time = data["start_time"]
        end_time = data["end_time"]
        doctor = data["doctor"]
        patient = data["patient"]

        # Rule 1: Date cannot be in the past
        if appointment_date < date.today():
            raise serializers.ValidationError(
                "Appointment cannot be booked in the past."
            )

        # Rule 2: End time must be after start time
        if end_time <= start_time:
            raise serializers.ValidationError(
                "End time must be after start time."
            )

        # Rule 3: Doctor conflict
        doctor_conflict = Appointment.objects.filter(
            doctor=doctor,
            appointment_date=appointment_date,
            start_time__lt=end_time,
            end_time__gt=start_time,
        )

        if self.instance:
            doctor_conflict = doctor_conflict.exclude(pk=self.instance.pk)

        if doctor_conflict.exists():
            raise serializers.ValidationError(
                "Doctor already has an appointment during this time."
            )

        # Rule 4: Patient conflict
        patient_conflict = Appointment.objects.filter(
            patient=patient,
            appointment_date=appointment_date,
            start_time__lt=end_time,
            end_time__gt=start_time,
        )

        if self.instance:
            patient_conflict = patient_conflict.exclude(pk=self.instance.pk)

        if patient_conflict.exists():
            raise serializers.ValidationError(
                "Patient already has an appointment during this time."
            )

        return data