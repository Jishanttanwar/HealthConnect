from django.shortcuts import render

# Create your views here.
from rest_framework import filters, viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .models import Notification
from .serializers import NotificationSerializer

class NotificationViewSet(viewsets.ModelViewSet):

    queryset = Notification.objects.select_related("user")

    serializer_class = NotificationSerializer

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    filterset_fields = [
        "notification_type",
        "is_read",
    ]

    search_fields = [
        "title",
        "message",
        "user__email",
    ]

    ordering_fields = [
        "created_at",
    ]

    ordering = [
        "-created_at",
    ]