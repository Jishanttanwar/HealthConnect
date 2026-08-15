from django.shortcuts import render

# Create your views here.
from django.db.models import Count
from django.utils import timezone

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from appointments.models import Appointment
from doctors.models import DoctorProfile
from lab_reports.models import LabReport
from medical_records.models import MedicalRecord
from patients.models import PatientProfile
from prescriptions.models import Prescription
from notifications.models import Notification


class AdminDashboardView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        if request.user.role != "ADMIN":
            return Response(
                {
                    "detail": "Only administrators can access this dashboard."
                },
                status=403,
            )

        today = timezone.localdate()

        data = {
            "total_patients": PatientProfile.objects.count(),

            "total_doctors": DoctorProfile.objects.count(),

            "total_appointments": Appointment.objects.count(),

            "appointments_today": Appointment.objects.filter(
                appointment_date=today
            ).count(),

            "completed_appointments": Appointment.objects.filter(
                status="COMPLETED"
            ).count(),

            "cancelled_appointments": Appointment.objects.filter(
                status="CANCELLED"
            ).count(),

            "total_prescriptions": Prescription.objects.count(),

            "total_lab_reports": LabReport.objects.count(),

            "total_medical_records": MedicalRecord.objects.count(),
        }

        return Response(data)


class DoctorDashboardView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        if request.user.role != "DOCTOR":
            return Response(
                {
                    "detail": "Only doctors can access this dashboard."
                },
                status=403,
            )

        today = timezone.localdate()

        appointments = Appointment.objects.filter(
            doctor__user=request.user
        )

        data = {
            "total_appointments": appointments.count(),

            "appointments_today": appointments.filter(
                appointment_date=today
            ).count(),

            "completed_appointments": appointments.filter(
                status="COMPLETED"
            ).count(),

            "scheduled_appointments": appointments.filter(
                status="SCHEDULED"
            ).count(),

            "confirmed_appointments": appointments.filter(
                status="CONFIRMED"
            ).count(),

            "cancelled_appointments": appointments.filter(
                status="CANCELLED"
            ).count(),

            "total_patients": appointments.values(
                "patient"
            ).distinct().count(),
        }

        return Response(data)

class PatientDashboardView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        if request.user.role != "PATIENT":
            return Response(
                {
                    "detail": "Only patients can access this dashboard."
                },
                status=403,
            )

        today = timezone.localdate()

        appointments = Appointment.objects.filter(
            patient__user=request.user
        )

        data = {
            "total_appointments": appointments.count(),

            "appointments_today": appointments.filter(
                appointment_date=today
            ).count(),

            "scheduled_appointments": appointments.filter(
                status="SCHEDULED"
            ).count(),

            "confirmed_appointments": appointments.filter(
                status="CONFIRMED"
            ).count(),

            "completed_appointments": appointments.filter(
                status="COMPLETED"
            ).count(),

            "cancelled_appointments": appointments.filter(
                status="CANCELLED"
            ).count(),

            "total_prescriptions": Prescription.objects.filter(
                encounter__appointment__patient__user=request.user
            ).count(),

            "total_lab_reports": LabReport.objects.filter(
                encounter__appointment__patient__user=request.user
            ).count(),

            "total_medical_records": MedicalRecord.objects.filter(
                patient__user=request.user
            ).count(),

            "unread_notifications": Notification.objects.filter(
                user=request.user,
                is_read=False
            ).count(),
        }

        return Response(data)