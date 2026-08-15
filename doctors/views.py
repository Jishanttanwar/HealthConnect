from django.shortcuts import render


from rest_framework import viewsets
from .models import DoctorProfile, DoctorAvailability
from .serializers import DoctorProfileSerializer
from .permissions import IsAdminOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend

from .availability_serializers import DoctorAvailabilitySerializer

# Create your views here.

class DoctorAvailabilityViewSet(viewsets.ModelViewSet):
    queryset = DoctorAvailability.objects.select_related("doctor","doctor__user",)

    serializer_class = DoctorAvailabilitySerializer
    permission_classes = [IsAdminOrReadOnly]

class DoctorProfileViewSet(viewsets.ModelViewSet):
    queryset = DoctorProfile.objects.select_related(
        "user",
        "department",
        "specialization",
    )
    serializer_class = DoctorProfileSerializer
    permission_classes = [IsAdminOrReadOnly]

    filter_backends = [DjangoFilterBackend]

    filterset_fields = {
        "department__name": ["exact"],
        "specialization__name": ["exact"],
    }


