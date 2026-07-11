from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import PatientProfileViewSet


router = DefaultRouter()
router.register("", PatientProfileViewSet)
urlpatterns = [

    path("", include(router.urls)),

]




