# Generated by Django 3.1.5 on 2021-02-08 22:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0004_auctionlisting_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bid',
            name='curentBid',
        ),
    ]
