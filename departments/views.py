from django.shortcuts import render

from rest_framework import viewsets
#from rest_framework.permissions import IsAuthenticated
from .models import Department
from .serializers import DepartmentSerializer
from .permissions import IsAdminOrReadOnly




# Create your views here.

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [IsAdminOrReadOnly]
