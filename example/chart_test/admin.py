from django.contrib import admin
from django_admin_chart.chart import BarAndPieChartAdmin, SingleBarChartAdmin, DuelBarChartAdmin

from .models import ChartTest


class ChartTestAdmin(BarAndPieChartAdmin):
    list_display = ('id', 'value', 'date',)
    list_display_links = ['value', 'id', ]
    list_per_page = 25

    inlines = []

    """ no need for chart here will update later """
    chart_url = '/view/chart/tests/test_chart/'
    # chart_url_2 = '/view/chart/tests/test_chart/'
    chart_url_2 = '/view/chart/tests/test_quantity_chart/'
    chart_filter_url = '/view/chart/tests/test_chart_filter/filter-options/'
    chart_select_filter = 'value'


admin.site.register(ChartTest, ChartTestAdmin)
