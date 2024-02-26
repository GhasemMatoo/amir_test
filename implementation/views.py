from django.shortcuts import render
from django.views.generic import ListView
from django.views import View
from django.contrib import messages

from implementation.models import (
    Performance, OperationCost, PriceList, ResourceAllocation,
    Machinery, Employee, Material
)
from implementation.forms import (
    PerformanceForm, MachineryForm, EmployeeForm, MaterialForm,
    OperationCostForm, PriceListForm, ResourceAllocationForm
)
from implementation.calculator import resource_allocation_calc, machinery_form_calc
# Create your views here.


class PerformanceFormViews(ListView):
    template_name = 'implementation/PerformanceForm.html'
    model = Performance
    form_class = PerformanceForm
    context_object_name = 'Performance'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        form = self.form_class()
        context = super().get_context_data(**kwargs)
        context['form'] = form
        return context

    def post(self, request, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            if None not in form.cleaned_data.values():
                form.save()
                messages.add_message(request, messages.SUCCESS, "داده وارد شده ثبت گردید.")
            else:
                messages.add_message(request, messages.WARNING, "لطفا مقادیر خالی ارسال نکنید.")
        else:
            messages.add_message(request, messages.ERROR, "داده وارد شده صحیح نیست و این داده ثبت نگردید.")
        return render(request, self.template_name)


class SourceFormViews(View):
    template_name = 'implementation/SourceForm.html'

    def get(self, request, **kwargs):
        machinery_form = MachineryForm()
        employee_form = EmployeeForm()
        material_form = MaterialForm()
        context = {
            'machinery_form': machinery_form,
            "employee_form": employee_form,
            "material_form": material_form
        }
        return render(request, self.template_name, context)

    def post(self, request, **kwargs):
        machinery_form = MachineryForm(request.POST)
        employee_form = EmployeeForm(request.POST)
        material_form = MaterialForm(request.POST)
        if 'machinery' in request.POST:
            if machinery_form.is_valid():
                if None not in machinery_form.cleaned_data.values():
                    machinery_form.save()
                    messages.add_message(request, messages.SUCCESS, "داده وارد شده ثبت گردید.")
                else:
                    messages.add_message(request, messages.WARNING, "لطفا مقادیر خالی ارسال نکنید.")
            else:
                messages.add_message(request, messages.ERROR, "داده وارد شده صحیح نیست و این داده ثبت نگردید.")
        elif 'employee' in request.POST:
            if employee_form.is_valid():
                if None not in employee_form.cleaned_data.values():
                    employee_form.save()
                    messages.add_message(request, messages.SUCCESS, "داده وارد شده ثبت گردید.")
                else:
                    messages.add_message(request, messages.WARNING, "لطفا مقادیر خالی ارسال نکنید.")
            else:
                messages.add_message(request, messages.ERROR, "داده وارد شده صحیح نیست و این داده ثبت نگردید.")
        elif 'material' in request.POST:
            if material_form.is_valid():
                if None not in material_form.cleaned_data.values():
                    material_form.save()
                    messages.add_message(request, messages.SUCCESS, "داده وارد شده ثبت گردید.")
                else:
                    messages.add_message(request, messages.WARNING, "لطفا مقادیر خالی ارسال نکنید.")
            else:
                messages.add_message(request, messages.ERROR, "داده وارد شده صحیح نیست و این داده ثبت نگردید.")
        context = {
            'machinery_form': machinery_form,
            "employee_form": employee_form,
            "material_form": material_form
        }
        return render(request, self.template_name, context)


class OperationCostFormViews(ListView):
    template_name = 'implementation/OperationCostForm.html'
    model = OperationCost
    form_class = OperationCostForm
    context_object_name = 'OperationCost'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        form = self.form_class()
        context = super().get_context_data(**kwargs)
        context['form'] = form
        return context

    def post(self, request, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            if None not in form.cleaned_data.values():
                form.save()
                messages.add_message(request, messages.SUCCESS, "داده وارد شده ثبت گردید.")
            else:
                messages.add_message(request, messages.WARNING, "لطفا مقادیر خالی ارسال نکنید.")
        else:
            messages.add_message(request, messages.ERROR, "داده وارد شده صحیح نیست و این داده ثبت نگردید.")
        return render(request, self.template_name)


class PriceListFormViews(ListView):
    template_name = 'implementation/PriceListForm.html'
    model = PriceList
    form_class = PriceListForm
    context_object_name = 'PriceList'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        form = self.form_class()
        context = super().get_context_data(**kwargs)
        context['form'] = form
        return context

    def post(self, request, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            if None not in form.cleaned_data.values():
                form.save()
                messages.add_message(request, messages.SUCCESS, "داده وارد شده ثبت گردید.")
            else:
                messages.add_message(request, messages.WARNING, "لطفا مقادیر خالی ارسال نکنید.")
        else:
            messages.add_message(request, messages.ERROR, "داده وارد شده صحیح نیست و این داده ثبت نگردید.")
        return render(request, self.template_name)


class ResourceAllocationFormViews(ListView):
    template_name = 'implementation/ResourceAllocation.html'
    model = ResourceAllocation
    form_class = ResourceAllocationForm
    context_object_name = 'ResourceAllocation'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        form = self.form_class()
        context = super().get_context_data(**kwargs)
        context['form'] = form
        return context

    def post(self, request, **kwargs):
        form = self.form_class(request.POST)
        object_list = ResourceAllocation.objects.all()
        context = self.get_context_data(object_list=object_list, **kwargs)
        if form.is_valid():
            dict_data = form.cleaned_data.values().mapping
            if request.POST['save_next']:
                instance = form.instance
                instance = resource_allocation_calc(instance, dict_data)
                instance.save()
                context["machinery_list"] = Machinery.objects.all()
                context["employee_list"] = Employee.objects.all()
                context["material_list"] = Material.objects.all()
                context["source_form"] = True
                context["instance_id"] = instance.id
                return render(request, self.template_name, context=context)
            else:
                messages.add_message(request, messages.WARNING, "لطفا مقادیر خالی ارسال نکنید.")
        elif form.data.get('save_list'):
            instance = ResourceAllocation.objects.get(id=form.data.get(' instance_id '))
            if instance:
                for key, val in form.data.items():
                    if ',' in key and val != "" and val.isnumeric():
                        item_id, item_name, item_amount = key.split(',')
                        machinery_form_calc(instance, item_name, item_amount, val)
                        instance.save()
                return render(request, self.template_name, context=context)
            else:
                messages.add_message(request, messages.ERROR, "داده وارد شده صحیح نیست و این داده ثبت نگردید.")
        else:
            messages.add_message(request, messages.ERROR, "داده وارد شده صحیح نیست و این داده ثبت نگردید.")
        return render(request, self.template_name)