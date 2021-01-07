from django import forms
from django.forms import widgets

from .models import Empleado


class EmpleadoForm(forms.ModelForm):
    """Form definition for Empleado."""

    class Meta:

        model = Empleado
        fields = (
            'first_name',
            'last_name',
            'job',
            'departamento',
            'habilidades',
        )

        widgets = {
            'habilidades': forms.CheckboxSelectMultiple()

        }
