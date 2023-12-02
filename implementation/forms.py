from django.forms import ModelForm
from implementation.models import (Performance, Machinery, Employee, Material, OperationCost, PriceList)


class PerformanceForm(ModelForm):
    class Meta:
        model = Performance
        fields = ["group", "typeـoperation", "amounts"]
