from django.db import models


class Balance(models.Model):
    tablename = "Balance"
    userId = models.IntegerField()
    currentBalance = models.DecimalField
    date = models.DateField()
