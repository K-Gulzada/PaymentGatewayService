from django.db import models


class PaymentStatus(models.Model):
    tablename = "PaymentStatus"
    statusCode = models.BigAutoField(primary_key=True)
    description = models.TextField
