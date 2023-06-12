from django.urls import path

from chart_test.test_statistics.test_statistics_data_view import test_statistics_data_view
from chart_test.test_statistics.test_statistics_quantity_view import test_statistics_quantity_view

# from  import test_statistics_data_view, test_statistics_quantity_view

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
    path(
        'test_quantity_chart/',
        test_statistics_quantity_view.get_data_chart,
        name='test-quantity-chart'
    ),
]
