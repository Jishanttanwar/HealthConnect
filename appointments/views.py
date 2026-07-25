from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets

from .models import Appointment
from .permissions import IsAuthenticatedUser
from .serializers import AppointmentSerializer


class AppointmentViewSet(viewsets.ModelViewSet):

    queryset = Appointment.objects.select_related(
        "doctor",
        "doctor__user",
        "patient",
        "patient__user",
    )

    serializer_class = AppointmentSerializer

    permission_classes = [IsAuthenticatedUser]