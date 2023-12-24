from django.urls import path
from .views import (
    PerformanceFormViews, SourceFormViews, OperationCostFormViews, PriceListFormViews, ResourceAllocationFormViews
)


app_name = 'implementation'

urlpatterns = [
    path('PerformanceForm/', PerformanceFormViews.as_view(), name="Performance_Forms"),
    path('SourceForm/', SourceFormViews.as_view(), name="Source_Forms"),
    path('OperationCostForm/', OperationCostFormViews.as_view(), name="OperationCost_Form"),
    path('PriceListForm/', PriceListFormViews.as_view(), name="PriceList_Form"),
    path('ResourceAllocationForm/', ResourceAllocationFormViews.as_view(), name="ResourceAllocation_Form"),
]
