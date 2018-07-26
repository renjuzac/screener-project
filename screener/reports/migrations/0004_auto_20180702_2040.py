# Generated by Django 2.0.6 on 2018-07-03 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0003_auto_20180702_2037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scan',
            name='description',
            field=models.CharField(help_text='scanner description', max_length=50),
        ),
        migrations.AlterField(
            model_name='scan',
            name='function',
            field=models.CharField(blank=True, help_text='scanner function', max_length=50, null=True),
        ),
    ]
