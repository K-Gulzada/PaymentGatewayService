from django.db import models


class Balance(models.Model):
    tablename = "Balance"
    userId = models.IntegerField()
    currentBalance = models.DecimalField(max_digits=16, decimal_places=2, null=True)
    date = models.DateField()
