from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Appointment
from .permissions import IsAuthenticatedUser
from .serializers import AppointmentSerializer
from patients.models import PatientProfile

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

class AppointmentViewSet(viewsets.ModelViewSet):
    serializer_class = AppointmentSerializer
    permission_classes = [IsAuthenticatedUser]

    def get_queryset(self):
        user = self.request.user
        queryset = Appointment.objects.select_related(
            "patient","patient__user","doctor","doctor__user",
        )

        if user.role == "ADMIN":

            return queryset

        elif user.role == "DOCTOR":

            return queryset.filter(doctor__user=user)

        elif user.role == "PATIENT":

            return queryset.filter(patient__user=user)

        return queryset.none()


    def perform_create(self, serializer):
        user = self.request.user
        if user.role == "PATIENT":
            patient = PatientProfile.objects.get(user=user)
            serializer.save(patient=patient)
        else:
            serializer.save()


filter_backends = [
    DjangoFilterBackend,
    filters.SearchFilter,
    filters.OrderingFilter,
]
filterset_fields = [
    "status",
    "appointment_date",
]
search_fields = [
    "doctor__user__username",
    "patient__user__username",
]
ordering_fields = [
    "appointment_date",
    "created_at",
]
ordering = [
    "appointment_date", "start_time"
    ]

