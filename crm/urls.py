from django.urls import re_path as url, include
from rest_framework.routers import DefaultRouter
from .views import BeneficiarioViewSet, EmpleadoViewSet

router = DefaultRouter()
router.register(r"beneficiario", BeneficiarioViewSet, basename="beneficiario"),
router.register(r"empleado", EmpleadoViewSet, basename="empleado")

urlpatterns = [url(r"^", include(router.urls))]
