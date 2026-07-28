from django.shortcuts import render

# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets
from .models import LabReport
from .serializers import LabReportSerializer
from .permissions import IsDoctorOrAdmin


class LabReportViewSet(viewsets.ModelViewSet):

    queryset = LabReport.objects.select_related(
        "encounter",
        "encounter__appointment",
        "encounter__appointment__doctor",
        "encounter__appointment__patient",
    )

    serializer_class = LabReportSerializer

    permission_classes = [IsDoctorOrAdmin]

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    filterset_fields = [
        "status",
        "report_date",
    ]

    search_fields = [
        "report_name",
        "encounter__appointment__patient__user__username",
        "encounter__appointment__doctor__user__username",
    ]

    ordering_fields = [
        "report_date",
        "created_at",
    ]

    ordering = [
        "-report_date",
    ]