from django.urls import path, include

from rest_framework.routers import DefaultRouter
from .views import DoctorProfileViewSet, DoctorAvailabilityViewSet


router = DefaultRouter()
router.register(
    r"",
    DoctorProfileViewSet,
    basename="doctor"
)
router.register(
    "availability",
    DoctorAvailabilityViewSet,
    basename="doctor-availability",
)

urlpatterns = [
    path("", include(router.urls)),

]