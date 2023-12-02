from django.urls import path
from .views import (PerformanceFormViews, SourceFormViews)


app_name = 'implementation'

urlpatterns = [
    path('PerformanceForm/', PerformanceFormViews.as_view(), name="Performance_Forms"),
    path('SourceForm/', SourceFormViews.as_view(), name="Source_Forms"),
]
