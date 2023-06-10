from django.contrib import admin

from .models import ChartTest
from django_admin_chart.chart import chart


class ChartTestAdmin(admin.ModelAdmin):
    list_display = ('id', 'value')
    list_display_links = ['value', 'id', ]
    list_per_page = 25

    inlines = []

    """ no need for chart here will update later """

    # change_list_template = 'admin/supplier_statistics.html'
    def changelist_view(self, request, extra_context=None):
        # chart()
        extra_context = extra_context or {}
        extra_context['my_param'] = 'my_value'
        self.change_list_template = 'django_admin_chart/duel_bar_chart.html'
        # self.change_list_template = 'file.html'
        # self.change_list_template = '../folders/file.html'
        # self.change_list_template = 'duel_bar_chart.html'
        # django_admin_chart
        # type_chart = duel_bar_chart, duel_pie_chart, duel_one_bar_one_pie, bar_chart, pie_chart
        return super().changelist_view(request, extra_context=extra_context)


admin.site.register(ChartTest, ChartTestAdmin)
