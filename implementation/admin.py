from django.contrib import admin
from django.forms.widgets import NumberInput
from django.db import models
from .models import (Performance, Machinery, Employee,
                     Material, OperationCost, PriceList, ResourceAllocation)


class AmountsSplit:
    empty_value_display = "-خالی-"
    formfield_overrides = {
        models.IntegerField: {'widget': NumberInput(attrs={"size": "60"})},
    }

    def view_amounts_split(self, obj):
        if obj.amounts:
            return f'{obj.amounts:,}'


@admin.register(Performance)
class PerformanceAdmin(AmountsSplit, admin.ModelAdmin):
    list_display = ["group", "typeـoperation", "view_amounts_split"]
    search_fields = ["group", "typeـoperation"]


@admin.register(Machinery)
class MachineryAdmin(AmountsSplit, admin.ModelAdmin):
    list_display = ["car_name", "view_amounts_split"]
    search_fields = ["car_name"]


@admin.register(Employee)
class EmployeeAdmin(AmountsSplit, admin.ModelAdmin):
    list_display = ["expertise_name", "view_amounts_split"]
    search_fields = ["expertise_name"]


@admin.register(Material)
class MaterialAdmin(AmountsSplit, admin.ModelAdmin):
    list_display = ["material_use", "view_amounts_split"]
    search_fields = ["material_use"]


@admin.register(OperationCost)
class OperationCostAdmin(AmountsSplit, admin.ModelAdmin):
    list_display = ["machinery_name", "uint", "view_amounts_split"]
    search_fields = ["machinery_name"]


@admin.register(PriceList)
class OperationCostAdmin(AmountsSplit, admin.ModelAdmin):
    list_display = ["chapter_number", "item_number", "description",
                    "unit", "amounts"]
    search_fields = ["item_number", "description"]


@admin.register(ResourceAllocation)
class ResourceAllocationAdmin(admin.ModelAdmin):
    list_display = ["performance", "hours_normal_implement_enterprise_machines"]
    search_fields = ["performance", "hours_normal_implement_enterprise_machines"]


admin.site.site_header = "پنل مدیریتی"
admin.site.site_title = "سامانه مدیریت"
admin.site.index_title = "سامانه مدیریت"