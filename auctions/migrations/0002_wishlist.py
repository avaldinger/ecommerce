# Generated by Django 3.1.5 on 2021-02-12 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WishList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timeStamp', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]