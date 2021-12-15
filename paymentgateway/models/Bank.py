from django.db import models


class Bank(models.Model):
    tablename = "Bank"
    config = models.CharField(max_length=255)
