from django.shortcuts import render

from rest_framework import viewsets
from .models import Specialization
from .serializers import SpecializationSerializer
from .permissions import IsAdminOrReadOnly


# Create your views here.

class SpecializationViewSet(viewsets.ModelViewSet):
    queryset = Specialization.objects.all()
    serializer_class = SpecializationSerializer
    permission_classes = [IsAdminOrReadOnly]
