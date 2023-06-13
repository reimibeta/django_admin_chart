# Install
    pip3 install django-admin-chart

# Usage
## setup statistics and url is in example folder

# In admin
    class ChartTestAdmin(BarAndPieChartAdmin):
        list_display = ('id', 'value', 'date',)
        list_display_links = ['value', 'id', ]
        list_per_page = 25
    
        inlines = []
    
        """ add this to admin """
        chart_url = '/view/chart/tests/test_chart/'
        chart_url_2 = '/view/chart/tests/test_quantity_chart/'
        chart_filter_url = '/view/chart/tests/test_chart_filter/filter-options/'
        chart_select_filter = 'value'

    admin.site.register(ChartTest, ChartTestAdmin)

## check on example to test how it works.
### create statistics
### create url
### add params to admin
    