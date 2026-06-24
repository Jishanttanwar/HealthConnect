from django.shortcuts import render


from rest_framework import viewsets
from .models import DoctorProfile
from .serializers import DoctorProfileSerializer
from .permissions import IsAdminOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend



# Create your views here.

class DoctorProfileViewSet(viewsets.ModelViewSet):
    queryset = DoctorProfile.objects.select_related('user', 'department', 'specialization')
    serializer_class = DoctorProfileSerializer
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {'department__name': ['exact'], 'specialization__name': ['exact']}


