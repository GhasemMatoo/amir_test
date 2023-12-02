from django.forms import ModelForm
from implementation.models import (Performance, Machinery, Employee, Material, OperationCost, PriceList)


class PerformanceForm(ModelForm):
    class Meta:
        model = Performance
        fields = ["group", "typeـoperation", "amounts"]


class MachineryForm(ModelForm):
    class Meta:
        model = Machinery
        fields = ["car_name", "amounts"]


class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = ["expertise_name", "amounts"]


class MaterialForm(ModelForm):
    class Meta:
        model = Material
        fields = ["material_use", "amounts"]


class OperationCostForm(ModelForm):
    class Meta:
        model = OperationCost
        fields = ["machinery_name", "uint", "amounts"]


class PriceListForm(ModelForm):
    class Meta:
        model = PriceList
        fields = ["chapter_number", "item_number", "description", "unit", "amounts"]
