from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views import View
from django.contrib import messages

from implementation.models import (Performance, Machinery, Employee, Material, OperationCost, PriceList)
from implementation.forms import PerformanceForm, MachineryForm, EmployeeForm, MaterialForm
# Create your views here.


class PerformanceFormViews(ListView):
    template_name = 'implementation/PerformanceForm.html'
    model = Performance
    form_class = PerformanceForm
    context_object_name = 'performance'

    def get(self, request, **kwargs):
        form = self.form_class()
        context = {'form': form}
        return render(request, self.template_name, context)

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
        context = {'form': form}
        return render(request, self.template_name, context)


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
