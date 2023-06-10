from django.urls import path

from chart_test.statistics import test_statistics_data_view

urlpatterns = [
    path(
        'test_chart_filter/filter-options/',
        test_statistics_data_view.get_filter_chart,
        name='test-filter-options'
    ),
    path(
        'test_chart/',
        test_statistics_data_view.get_data_chart,
        name='test-chart'
    ),
    # path(
    #     'supplier_quantity_chart/',
    #     supplier_statistics_quantity_view.get_data_chart,
    #     name='supplier-quantity-chart'
    # ),
]
