from django.shortcuts import render

# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets
from .models import MedicalRecord
from .permissions import IsDoctorOrAdmin
from .serializers import MedicalRecordSerializer

class MedicalRecordViewSet(viewsets.ModelViewSet):

    queryset = MedicalRecord.objects.select_related(
        "patient",
        "patient__user",
    )

    serializer_class = MedicalRecordSerializer

    permission_classes = [IsDoctorOrAdmin]

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    filterset_fields = [
        "status",
    ]

    search_fields = [
        "patient__user__username",
        "patient__user__email",
        "diagnosis",
    ]

    ordering_fields = [
        "created_at",
    ]

    ordering = [
        "-created_at",
    ]