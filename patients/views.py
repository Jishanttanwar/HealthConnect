from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets , filters 
from .models import PatientProfile
from .serializers import PatientProfileSerializer
from .permissions import IsAdminOrReadOnly

class PatientProfileViewSet(viewsets.ModelViewSet):
    queryset = PatientProfile.objects.select_related("user")
    serializer_class = PatientProfileSerializer
    permission_classes = [IsAdminOrReadOnly]


#suggested by chatgpt for filtering, searching and ordering
    filter_backends = [

        DjangoFilterBackend,

        filters.SearchFilter,

        filters.OrderingFilter,

    ]

    filterset_fields = [

        "blood_group",

        "gender",

    ]

    search_fields = [

        "user__username",

        "user__email",

    ]

    ordering_fields = [

        "created_at",

        "updated_at",

    ]

    ordering = ["-created_at"]
