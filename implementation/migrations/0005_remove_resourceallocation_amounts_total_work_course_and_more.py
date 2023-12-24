# Generated by Django 4.1 on 2023-12-24 17:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('implementation', '0004_resourceallocation_performance_part_performance_unit'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resourceallocation',
            name='amounts_total_work_course',
        ),
        migrations.RemoveField(
            model_name='resourceallocation',
            name='description',
        ),
        migrations.RemoveField(
            model_name='resourceallocation',
            name='part',
        ),
        migrations.RemoveField(
            model_name='resourceallocation',
            name='typeـofـactivity',
        ),
        migrations.RemoveField(
            model_name='resourceallocation',
            name='unit',
        ),
        migrations.AddField(
            model_name='resourceallocation',
            name='Impact_factor',
            field=models.FloatField(blank=True, null=True, verbose_name='ضریب تأثیر'),
        ),
        migrations.AddField(
            model_name='resourceallocation',
            name='employee',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='implementation.employee'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='resourceallocation',
            name='machinery',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='implementation.machinery'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='resourceallocation',
            name='material',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='implementation.material'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='resourceallocation',
            name='percents_employee',
            field=models.IntegerField(blank=True, null=True, verbose_name='درصد نرم نیروی انسانی '),
        ),
        migrations.AddField(
            model_name='resourceallocation',
            name='percents_machinery',
            field=models.IntegerField(blank=True, null=True, verbose_name='درصد ماشین'),
        ),
        migrations.AddField(
            model_name='resourceallocation',
            name='percents_material',
            field=models.IntegerField(blank=True, null=True, verbose_name='درصد نرم مصالح'),
        ),
        migrations.AddField(
            model_name='resourceallocation',
            name='performance',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='implementation.performance'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='performance',
            name='group',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='گروه احجام اجرایی'),
        ),
    ]