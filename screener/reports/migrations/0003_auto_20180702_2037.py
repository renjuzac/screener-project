# Generated by Django 2.0.6 on 2018-07-03 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0002_auto_20180627_2234'),
    ]

    operations = [
        migrations.AddField(
            model_name='scan',
            name='function',
            field=models.CharField(blank=True, help_text='scanner function', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='scan',
            name='description',
            field=models.CharField(help_text='scanner description', max_length=20),
        ),
    ]
