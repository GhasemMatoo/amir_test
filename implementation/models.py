from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Performance(models.Model):
    group = models.CharField(max_length=250, blank=True, null=True, verbose_name=_("احجام اجرایی"))
    typeـoperation = models.CharField(max_length=250, blank=True, null=True, verbose_name=_("نوع عملیات"))
    amounts = models.IntegerField(blank=True, null=True, verbose_name=_("مقادیر"))

    def __str__(self):
        return f'{self.group} {self.typeـoperation}'

    class Meta:
        verbose_name = _("احجام اجرایی پروژه")
        verbose_name_plural = _("احجام اجرایی پروژها")


class Machinery(models.Model):
    car_name = models.CharField(max_length=250, blank=True, null=True, verbose_name=_("نام ماشین‌آلات"))
    amounts = models.IntegerField(blank=True, null=True, verbose_name=_("بهای کرایه ماهانه"))

    def __str__(self):
        return self.car_name

    class Meta:
        verbose_name = _("ماشین‌آلات")
        verbose_name_plural = _("ماشین‌آلات‌ها")


class Employee(models.Model):
    expertise_name = models.CharField(max_length=250, blank=True, null=True, verbose_name=_("نام‌تخصوص"))
    amounts = models.IntegerField(blank=True, null=True, verbose_name=_(" هزینه ماهانه"))

    def __str__(self):
        return self.expertise_name

    class Meta:
        verbose_name = _("کارمند")
        verbose_name_plural = _("کارمندان")


class Material(models.Model):
    material_use = models.CharField(max_length=250, blank=True, null=True, verbose_name=_("مواد و مصالح مصرفی"))
    amounts = models.IntegerField(blank=True, null=True, verbose_name=_(" هزینه تهیه یاخرید"))

    def __str__(self):
        return self.material_use

    class Meta:
        verbose_name = _("مواد و مصالح")
        verbose_name_plural = _("مواد و مصالح")


class OperationCost(models.Model):
    machinery_name = models.ForeignKey(Machinery, verbose_name=_("نام ماشین‌آلات"), on_delete=models.CASCADE,
                                       related_name="machinery_names")
    uint = models.IntegerField(blank=True, null=True, verbose_name=_("واحد"))
    amounts = models.IntegerField(blank=True, null=True, verbose_name=_("بهای‌واحد عملیات اجرای"))

    def __str__(self):
        return f'{self.machinery_name}{self.uint}'

    class Meta:
        verbose_name = _("هزینه عملیات اجرایی")
        verbose_name_plural = _("هزینه‌های عملیات اجرایی ")

