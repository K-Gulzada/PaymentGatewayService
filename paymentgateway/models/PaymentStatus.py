from django.db import models


class PaymentStatus(models.Model):
    tablename = "PaymentStatus"
    id = models.BigAutoField(primary_key=True)
    status = models.CharField(max_length=255, null=True)
    description = models.TextField(null=True)
