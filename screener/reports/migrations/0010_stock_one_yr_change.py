# Generated by Django 2.0.6 on 2018-07-11 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0009_stock_aquirersmultiple'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='one_yr_change',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
