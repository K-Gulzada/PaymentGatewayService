from django.db import models


class PaymentMethod(models.Model):
    tablename = "PaymentMethods"
    methodName = models.CharField(max_length=100)
