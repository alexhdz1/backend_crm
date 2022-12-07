from django.db import models


class Empleado(models.Model):

    name = models.CharField(max_length=100, verbose_name="Nombre")
    father_name = models.CharField(max_length=100, verbose_name="Primer apellido")
    mother_name = models.CharField(max_length=100, verbose_name="Segundo apellido")
    job = models.CharField(max_length=100, verbose_name="Puesto de trabajo")
    salary = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Salario"
    )
    status = models.BooleanField(default=True, verbose_name="Estatus")
    contract_day = models.DateTimeField(
        auto_now=False, verbose_name="Fecha de contrato"
    )
    date_name = models.DateTimeField(auto_now=False, verbose_name="Fecha de nacimiento")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:

        db_table = "empleado"
        verbose_name = "Empleado"
        verbose_name_plural = "Empleados"

    def __str__(self):
        return self.name


class Beneficiario(models.Model):

    employee = models.ForeignKey(
        Empleado, on_delete=models.CASCADE, verbose_name="Empleado"
    )
    name = models.CharField(max_length=100, verbose_name="Nombre")
    father_name = models.CharField(max_length=100, verbose_name="Primer apellido")
    mother_name = models.CharField(max_length=100, verbose_name="Segundo apellido")
    partent = models.CharField(max_length=100, verbose_name="Parentesco")
    sex = models.CharField(max_length=20, verbose_name="Sexo")
    date_name = models.DateTimeField(auto_now=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:

        db_table = "beneficiario"
        verbose_name = "Beneficiario"
        verbose_name_plural = "Beneficiarios"

    def __str__(self):
        return self.name
