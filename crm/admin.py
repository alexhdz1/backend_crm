from django.contrib import admin
from django.contrib.sites.models import Site
from .models import Empleado, Beneficiario

# Unregister default models from admin
admin.site.unregister(Site)


@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
    )


@admin.register(Beneficiario)
class BeneficiarioAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
    )
