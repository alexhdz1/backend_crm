from rest_framework import serializers
from crm.models import Empleado, Beneficiario


class EmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleado
        exclude = (
            "created_at",
            "updated_at",
        )


class BeneficiarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Beneficiario
        exclude = (
            "created_at",
            "updated_at",
        )
