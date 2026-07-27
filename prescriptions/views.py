from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Prescription
from .serializers import PrescriptionSerializer
from .permissions import IsDoctorOrAdmin
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

class PrescriptionViewSet(viewsets.ModelViewSet):
#This below querysset avoids unnecessary database queries.
    queryset = Prescription.objects.select_related(
        "encounter",
        "encounter__appointment",
        "encounter__appointment__doctor",
        "encounter__appointment__patient",
    ).prefetch_related("items")

    serializer_class = PrescriptionSerializer
    permission_classes = [IsDoctorOrAdmin]

filter_backends = [
    DjangoFilterBackend,
    filters.SearchFilter,
    filters.OrderingFilter,
]
filterset_fields = [
    "encounter",
]
search_fields = [
    "encounter__appointment__doctor__user__username",
    "encounter__appointment__patient__user__username",
]
ordering_fields = [
    "created_at",
]
ordering = [
    "-created_at",
]