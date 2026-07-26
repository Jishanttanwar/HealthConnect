from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import EncounterViewSet

router = DefaultRouter()
router.register("", EncounterViewSet)

urlpatterns = [
    path("", include(router.urls)),
]