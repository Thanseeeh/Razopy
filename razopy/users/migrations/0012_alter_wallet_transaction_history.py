# Generated by Django 4.1.8 on 2023-04-28 12:37

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_wallet_razor_pay_order_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wallet',
            name='transaction_history',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), default=list, size=None),
        ),
    ]
