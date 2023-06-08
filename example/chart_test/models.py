from django.db import models


class ChartTest(models.Model):
    value = models.TextField(blank=True, null=True)

    def __str__(self):
        return "{}".format(self.value)
