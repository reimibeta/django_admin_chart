from django_admin_chart.statistics import StatisticsData, StatisticsChart
from chart_test.models import ChartTest


# quantity
class TestStatisticsQuantity(StatisticsData):
    def get_filter(self):
        pass

    def get_data(self, *args, **kwargs):
        data = ChartTest.objects.filter(date__year=kwargs.get('year'))
        if 'value' in kwargs and kwargs.get("value") != "":
            data = data.filter(value=kwargs.get("value"))

        return data


class TestStatisticsQuantityView(StatisticsChart):
    ssq = TestStatisticsQuantity()

    def get_filter_chart(self, request):
        pass

    def get_data_chart(self, request):
        year = request.GET['year']
        value = request.GET['value']
        # for data in self.data.get_data():
        data = self.ssq.get_data(year=year, value=value)

        return self.chart.chart_pie(
            title=f"Quantity in {year}",
            labels=['Total', ],
            colors=['rgba(0, 165, 58, 0.9)', ],
            data=[
                data.count(),
            ],
            extra={}
        )


test_statistics_quantity_view = TestStatisticsQuantityView()
