# Generated by Django 2.0.6 on 2018-07-28 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0015_auto_20180725_2255'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='compositeMetric',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
