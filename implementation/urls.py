from django.urls import path, include
from .views import (PerformanceFormViews)


app_name = 'implementation'

urlpatterns = [
    path('PerformanceForm/', PerformanceFormViews.as_view(), name="Performance_Forms"),
]
