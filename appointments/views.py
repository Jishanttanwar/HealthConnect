from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets

from .models import Appointment
from .permissions import IsAuthenticatedUser
from .serializers import AppointmentSerializer


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
