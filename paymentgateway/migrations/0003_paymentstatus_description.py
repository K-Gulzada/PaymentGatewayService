# Generated by Django 4.0 on 2021-12-27 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paymentgateway', '0002_balance_currentbalance'),
    ]

    operations = [
        migrations.AddField(
            model_name='paymentstatus',
            name='description',
            field=models.TextField(null=True),
        ),
    ]