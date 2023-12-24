# Generated by Django 4.1 on 2023-12-24 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('implementation', '0003_pricelist'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResourceAllocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='تاریخ بروزرسانی ')),
                ('part', models.CharField(blank=True, max_length=250, null=True, verbose_name='بخش')),
                ('typeـofـactivity', models.CharField(blank=True, max_length=250, null=True, verbose_name='نوع فعالیت')),
                ('unit', models.CharField(blank=True, max_length=250, null=True, verbose_name='واحد')),
                ('description', models.CharField(blank=True, max_length=250, null=True, verbose_name='شرح')),
                ('amounts_total_work_course', models.IntegerField(blank=True, null=True, verbose_name='مقادیر کل کار انجام شده در دوره (ریال)')),
                ('amounts_total_work_contractors', models.IntegerField(blank=True, null=True, verbose_name='مقادیر کار انجام شده  توسط پیمانکاران در دوره (ریال)')),
                ('active_day_shift', models.IntegerField(blank=True, null=True, verbose_name='تعداد روزهای فعال شیفت روز')),
                ('active_night_shift', models.IntegerField(blank=True, null=True, verbose_name='تعداد روزهای فعال شیفت شب')),
                ('number_work_shifts', models.CharField(blank=True, max_length=250, null=True, verbose_name='تعداد شیفت کاری')),
                ('day_shift_hours', models.IntegerField(blank=True, null=True, verbose_name='ساعت کاری شیفت روز')),
                ('night_shift_hours', models.IntegerField(blank=True, null=True, verbose_name='ساعت کاری شیفت شب')),
                ('number_active_shifts', models.IntegerField(blank=True, null=True, verbose_name='تعداد شیفت فعال')),
                ('carrying_distance', models.FloatField(blank=True, null=True, verbose_name='فاصله حمل')),
                ('number_services_hour', models.IntegerField(blank=True, null=True, verbose_name='تعداد سرویس در ساعت')),
                ('hours_normal_implement_enterprise_machines', models.FloatField(blank=True, null=True, verbose_name='نرم ساعتی اجرا شده توسط ماشین آلات سازمانی')),
                ('amounts', models.IntegerField(blank=True, null=True, verbose_name='بهاي واحد (ریال)')),
            ],
            options={
                'verbose_name': 'اطلاعات ورودی تخصیص منابع',
                'verbose_name_plural': 'اطلاعاتهای ورودی تخصیص منابع ',
            },
        ),
        migrations.AddField(
            model_name='performance',
            name='part',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='بخش '),
        ),
        migrations.AddField(
            model_name='performance',
            name='unit',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='واحد'),
        ),
    ]