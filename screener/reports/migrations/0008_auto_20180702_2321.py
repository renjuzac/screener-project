# Generated by Django 2.0.6 on 2018-07-03 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0007_auto_20180702_2311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='symbol',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]