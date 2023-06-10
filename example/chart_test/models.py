from django.db import models


class ChartTest(models.Model):
    date = models.DateField(blank=True, null=True)
    value = models.TextField(blank=True, null=True)
    digit = models.IntegerField(default=0)

    def __str__(self):
        return "{}".format(self.value)
