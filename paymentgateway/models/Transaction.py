from django.db import models

from paymentgateway.models.Bank import Bank
from paymentgateway.models.PaymentMethod import PaymentMethod
from paymentgateway.models.PaymentStatus import PaymentStatus


class Transaction(models.Model):
    tablename = "Transactions"
    orderInfo = models.CharField(max_length=255)
    sum = models.IntegerField
    statusId = models.ForeignKey(PaymentStatus, on_delete=models.CASCADE)
    paymentMethodId = models.ForeignKey(PaymentMethod, on_delete=models.CASCADE)
    BankId = models.ForeignKey(Bank, on_delete=models.CASCADE)
    date = models.DateField()
