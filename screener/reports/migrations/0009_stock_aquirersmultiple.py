# Generated by Django 2.0.6 on 2018-07-06 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0008_auto_20180702_2321'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='aquirersMultiple',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
