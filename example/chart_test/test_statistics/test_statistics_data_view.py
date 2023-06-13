from django.db.models import Sum
from django.db.models.functions import ExtractMonth, ExtractYear
from django_admin_chart.chart_color import ChartColor
from django_admin_chart.statistics import StatisticsData, StatisticsChart
from chart_test.models import ChartTest


class TestStatisticsData(StatisticsData):

    def get_filter(self):
        grouped_data = ChartTest.objects \
            .annotate(year=ExtractYear('date')) \
            .values('year').order_by('-year').distinct()
        years = [data['year'] for data in grouped_data]

        select_filters = ['']
        ss = ChartTest.objects.all()
        for s in ss:
            select_filters.append(s.value)
        return {
            'years': years,
            'values': select_filters
        }

    def get_data(self, *args, **kwargs):
        data = ChartTest.objects.filter(date__year=kwargs.get("year"))  # .filter(status='COMPLETED')
        if 'value' in kwargs and kwargs.get("value") != "":
            data = data.filter(value=kwargs.get("value"))
        grouped_data = data.annotate(month=ExtractMonth('date')) \
            .values('month') \
            .annotate(amount=Sum('digit')) \
            .values('month', 'amount').order_by('month')
        return grouped_data


class TestStatisticsDataView(StatisticsChart):
    data = TestStatisticsData()

    def get_dataset(self, *args, **kwargs):
        year = kwargs.get('year')
        data_request_dict = self.chart.get_year_dict()

        for data in self.data.get_data(year=year):
            data_request_dict[self.chart.months[data['month'] - 1]] = round(data['amount'], 2)  # r = revenue

        data_dataset = self.chart.dataset(
            data_request_dict,
            # self.ss.get_data(year=year),
            'Test',
            ChartColor.COLOR_SUCCESS
        )
        return self.chart.chart(
            f"Product supply in {year}",
            [data_dataset],
            data_request_dict.keys(),
            {}
        )

    #

    def get_filter_chart(self, request):
        return self.chart.filter(self.data.get_filter())

    # @staff_member_required
    def get_data_chart(self, request):
        year = request.GET['year']
        value = request.GET['value']
        data_request_dict = self.chart.get_year_dict()
        for data in self.data.get_data(year=year, value=value):
            data_request_dict[self.chart.months[data['month'] - 1]] = round(data['amount'], 2)  # r = revenue

        data_dataset = self.chart.dataset(
            data_request_dict,
            'Test',
            ChartColor.COLOR_SUCCESS
        )
        return self.chart.chart(
            f"Product supply in {year}",
            [data_dataset],
            data_request_dict.keys(),
            {}
        )


test_statistics_data_view = TestStatisticsDataView()
