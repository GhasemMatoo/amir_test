# Generated by Django 4.1 on 2024-01-07 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('implementation', '0006_remove_resourceallocation_impact_factor_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resourceallocation',
            name='amounts',
        ),
        migrations.AddField(
            model_name='resourceallocation',
            name='total_work_contractors',
            field=models.IntegerField(blank=True, null=True, verbose_name='مقادیر کار انجام شده  توسط پیمانکاران در دوره (ریال)'),
        ),
        migrations.AlterField(
            model_name='resourceallocation',
            name='amounts_total_work_contractors',
            field=models.IntegerField(blank=True, null=True, verbose_name='مقادیر کار انجام شده در دوره (ریال)'),
        ),
    ]
