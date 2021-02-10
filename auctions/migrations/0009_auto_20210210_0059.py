# Generated by Django 3.1.5 on 2021-02-09 23:59

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0008_auto_20210210_0045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auctionlisting',
            name='price',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(0.01)]),
        ),
    ]