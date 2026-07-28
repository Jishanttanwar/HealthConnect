from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import LabReportViewSet

router = DefaultRouter()
router.register("", LabReportViewSet)

urlpatterns = [
    path("", include(router.urls)),
]