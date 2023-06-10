from django.contrib.admin.views.decorators import staff_member_required
from django.db.models import Sum, F, Case, When, DecimalField
from django.db.models.functions import ExtractMonth, ExtractYear
from django.http import JsonResponse
from django.shortcuts import render
from django_admin_chart.chart_color import ChartColor
from django_admin_chart.statistics import StatisticsData, StatisticsChart

from chart_test.models import ChartTest


# from applications.inventory.products.supply.class_models.supply import Supply
# from applications.suppliers.class_models.supplier import Supplier
# from utils.chart.chart_color import ChartColor
# from utils.chart.statistics import StatisticsData, StatisticsChart


class TestStatisticsData(StatisticsData):

    def get_filter(self):
        grouped_data = ChartTest.objects \
            .annotate(year=ExtractYear('date')) \
            .values('year').order_by('-year').distinct()
        years = [data['year'] for data in grouped_data]

        # suppliers = ['']
        # ss = Supplier.objects.all()
        # for s in ss:
        #     suppliers.append(s.name)
        return {
            'years': years,
            # 'suppliers': suppliers
        }

    def get_data(self, *args, **kwargs):
        data = ChartTest.objects.filter(date__year=kwargs.get("year"))  # .filter(status='COMPLETED')
        # if 'supplier' in kwargs and kwargs.get("supplier") != "":
        #     data = data.filter(supply_product__supplier__name=kwargs.get("supplier"))
        grouped_data = data.annotate(month=ExtractMonth('date')) \
            .values('month') \
            .annotate(amount=Sum((F('digit')))).values('month', 'amount').order_by('month')
        return grouped_data


class TestStatisticsDataView(StatisticsChart):
    ss = TestStatisticsData()

    def get_filter_chart(self, request):
        return self.chart.filter(self.ss.get_filter())

    # @staff_member_required
    def get_data_chart(self, request):

        year = request.GET['year']
        if request.method == 'GET' and 'supplier' in request.GET:
            supplier = request.GET['supplier']
        else:
            supplier = ""

        complete_request_dict = self.chart.get_year_dict()
        pending_request_dict = self.chart.get_year_dict()

        for data in self.ss.get_data(year=year, supplier=supplier):
            if data['status'] == "COMPLETED":
                complete_request_dict[self.chart.months[data['month'] - 1]] = round(data['amount'], 2)
            if data['status'] == "PENDING":
                pending_request_dict[self.chart.months[data['month'] - 1]] = round(data['amount'], 2)
        complete_dataset = self.chart.dataset(
            complete_request_dict,
            "Total supply complete amount in USD",
            ChartColor.COLOR_SUCCESS,
        )
        pending_dataset = self.chart.dataset(
            pending_request_dict,
            "Total supply pending amount in USD",
            ChartColor.COLOR_DANGER
        )
        return self.chart.chart(
            f"Product supply in {year}",
            [complete_dataset, pending_dataset],
            complete_request_dict.keys(),
            {}
        )


# quantity
# class SupplierStatisticsQuantity(StatisticsData):
#
#     def get_filter(self):
#         pass
#
#     def get_data(self, *args, **kwargs):
#         data = Supply.objects.filter(
#             request_date__year=kwargs.get("year"))  # .filter(order_payment__payment_status='PAID')
#         if 'supplier' in kwargs and kwargs.get("supplier") != "":
#             data = data.filter(supply_product__supplier__name=kwargs.get("supplier"))
#         grouped_data = data.annotate(month=ExtractMonth('request_date')) \
#             .values('month') \
#             .annotate(quantity=Sum('supply_product__quantity')) \
#             .values('month', 'quantity') \
#             .annotate(status=F('status')) \
#             .values('month', 'quantity', 'status') \
#             .order_by('month')
#         return grouped_data
#
#
# class SupplierStatisticsQuantityView(StatisticsChart):
#     ssq = SupplierStatisticsQuantity()
#
#     def get_filter_chart(self, request):
#         pass
#
#     # @staff_member_required
#     def get_data_chart(self, request):
#         year = request.GET['year']
#         if request.method == 'GET' and 'supplier' in request.GET:
#             supplier = request.GET['supplier']
#         else:
#             supplier = ""
#
#         complete_dict = self.chart.get_year_dict()
#
#         for data in self.ssq.get_data(year=year, supplier=supplier):
#             if data['status'] == "COMPLETED":
#                 complete_dict[self.chart.months[data['month'] - 1]] = data['quantity']
#         dataset = self.chart.dataset(complete_dict, "Total quantity")
#         return self.chart.chart(
#             f"Supply quantity in {year}",
#             [dataset], complete_dict.keys(),
#             {}
#         )


test_statistics_data_view = TestStatisticsDataView()
# supplier_statistics_quantity_view = SupplierStatisticsQuantityView()
