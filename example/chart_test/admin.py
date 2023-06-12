from django.contrib import admin
from django_admin_chart.chart import BarAndPieChartAdmin, SingleChartAdmin, DuelChartAdmin

from .models import ChartTest


# class ChartAdmin(admin.ModelAdmin):
#     chart_url = None
#     chart_url_2 = None
#     chart_filter_url = None
#     chart_template = None
#     chart_select_filter = None
#
#     def changelist_view(self, request, extra_context=None):
#         extra_context = extra_context or {}
#
#         extra_context['url'] = self.chart_url
#         # duel chart or one bar and one pie chart has 2 links
#         if self.chart_url_2:
#             extra_context['url2'] = self.chart_url_2
#
#         extra_context['url_filter'] = self.chart_filter_url
#
#         extra_context['select_filter'] = self.chart_select_filter
#
#         self.change_list_template = self.chart_template
#
#         return super().changelist_view(request, extra_context=extra_context)
#
#
# # raise ValueError('Chart filter url not found.')
# class SingleChartAdmin(ChartAdmin):
#     chart_template = 'django_admin_chart/one_bar_chart.html'
#
#
# class DuelChartAdmin(ChartAdmin):
#     chart_template = 'django_admin_chart/duel_bar_chart.html'
#
#
# class BarAndPieChartAdmin(ChartAdmin):
#     chart_template = 'django_admin_chart/one_bar_one_pie_chart.html'


# admin.ModelAdmin
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
    # chart_template = 'django_admin_chart/one_bar_chart.html'

    # change_list_template = 'admin/supplier_statistics.html'
    # def changelist_view(self, request, extra_context=None):
    #     extra_context = extra_context or {}
    #     extra_context['url'] = '/view/chart/tests/test_chart/'
    #     # extra_context['url2'] = '/view/chart/tests/test_chart/'
    #     extra_context['url_filter'] = '/view/chart/tests/test_chart_filter/filter-options/'
    #     extra_context['select_filter'] = 'value'
    #     self.change_list_template = 'django_admin_chart/one_bar_chart.html'
    #     # type_chart = duel_bar_chart, duel_pie_chart, duel_one_bar_one_pie, bar_chart, pie_chart
    #     return super().changelist_view(request, extra_context=extra_context)


admin.site.register(ChartTest, ChartTestAdmin)
