from django.contrib import admin

from .models import ChartTest
from django_admin_chart.chart import chart


class ChartTestAdmin(admin.ModelAdmin):
    list_display = ('id', 'value', 'date', )
    list_display_links = ['value', 'id', ]
    list_per_page = 25

    inlines = []

    """ no need for chart here will update later """

    # change_list_template = 'admin/supplier_statistics.html'
    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        extra_context['url'] = '/view/chart/tests/test_chart/'
        # extra_context['url2'] = '/view/chart/tests/test_chart/'
        extra_context['url_filter'] = '/view/chart/tests/test_chart_filter/filter-options/'
        extra_context['select_filter'] = 'value'
        self.change_list_template = 'django_admin_chart/one_bar_chart.html'
        # type_chart = duel_bar_chart, duel_pie_chart, duel_one_bar_one_pie, bar_chart, pie_chart
        return super().changelist_view(request, extra_context=extra_context)


admin.site.register(ChartTest, ChartTestAdmin)
