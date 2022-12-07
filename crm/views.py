from django.shortcuts import render
from .models import Empleado, Beneficiario
from rest_framework.viewsets import ModelViewSet
from .serializers import EmpleadoSerializer, BeneficiarioSerializer
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.


class EmpleadoViewSet(ModelViewSet):

    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = [
        "id",
        "name",
        "father_name",
        "mother_name",
        "salary",
        "job",
        "salary",
        "status",
        "contract_day",
        "date_name",
        "created_at",
        "updated_at",
    ]


class BeneficiarioViewSet(ModelViewSet):

    queryset = Beneficiario.objects.all()
    serializer_class = BeneficiarioSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = [
        "id",
        "name",
        "father_name",
        "mother_name",
        "partent",
        "sex",
        "date_name",
        "created_at",
        "updated_at",
    ]
