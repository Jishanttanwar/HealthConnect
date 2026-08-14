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