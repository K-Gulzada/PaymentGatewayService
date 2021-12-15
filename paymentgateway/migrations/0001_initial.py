# Generated by Django 4.0 on 2021-12-15 13:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Balance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userId', models.IntegerField()),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('config', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='PaymentMethod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('methodName', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='PaymentStatus',
            fields=[
                ('statusCode', models.BigAutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orderInfo', models.CharField(max_length=255)),
                ('date', models.DateField()),
                ('BankId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='paymentgateway.bank')),
                ('paymentMethodId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='paymentgateway.paymentstatus')),
                ('statusId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='paymentgateway.paymentmethod')),
            ],
        ),
    ]