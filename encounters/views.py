from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .models import Encounter
from .serializers import EncounterSerializer
from .permissions import IsDoctorOrAdmin


class EncounterViewSet(viewsets.ModelViewSet):
    queryset = Encounter.objects.select_related(
        "appointment",
        "appointment__doctor",
        "appointment__patient",
    )

    serializer_class = EncounterSerializer

    permission_classes = [IsDoctorOrAdmin]