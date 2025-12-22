from django.db import models


class ChartTest(models.Model):
    date = models.DateField(blank=True, null=True)
    value = models.TextField(blank=True, null=True)
    digit = models.DecimalField(default=0, max_digits=10, decimal_places=2)

    def __str__(self):
        return "{}".format(self.value)
