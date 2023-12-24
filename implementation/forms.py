from django.forms import ModelForm, Textarea
from implementation.models import (
    Performance, Machinery, Employee, Material, OperationCost, PriceList, ResourceAllocation
)


class PerformanceForm(ModelForm):
    class Meta:
        model = Performance
        fields = ["group", "part", "typeـoperation","unit", "amounts"]


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


class ResourceAllocationForm(ModelForm):
    class Meta:
        model = ResourceAllocation
        fields = [
            "performance",
            "amounts_total_work_contractors", "active_day_shift",
            "active_night_shift", "number_work_shifts",
            "day_shift_hours", "night_shift_hours", "number_active_shifts",
            "carrying_distance", "number_services_hour",
            "hours_normal_implement_enterprise_machines",
            "amounts", "machinery", "percents_machinery",
            "material", "percents_material", "employee",
            "percents_employee"
        ]
