from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("تاریخ ثبت"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("تاریخ بروزرسانی "))

    class Meta:
        abstract = True


class Performance(BaseModel):
    group = models.CharField(max_length=250, blank=True, null=True, verbose_name=_("احجام اجرایی"))
    typeـoperation = models.CharField(max_length=250, blank=True, null=True, verbose_name=_("نوع عملیات"))
    amounts = models.IntegerField(blank=True, null=True, verbose_name=_("مقادیر"))

    def __str__(self):
        return f'{self.group} {self.typeـoperation}'

    class Meta:
        verbose_name = _("احجام اجرایی پروژه")
        verbose_name_plural = _("احجام اجرایی پروژها")


class Machinery(BaseModel):
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


class Material(BaseModel):
    material_use = models.CharField(max_length=250, blank=True, null=True, verbose_name=_("مواد و مصالح مصرفی"))
    amounts = models.IntegerField(blank=True, null=True, verbose_name=_(" هزینه تهیه یاخرید"))

    def __str__(self):
        return self.material_use

    class Meta:
        verbose_name = _("مواد و مصالح")
        verbose_name_plural = _("مواد و مصالح")


class OperationCost(BaseModel):
    machinery_name = models.CharField(max_length=250, blank=True, null=True, verbose_name=_("نام ماشین‌آلات"))
    uint = models.IntegerField(blank=True, null=True, verbose_name=_("واحد"))
    amounts = models.IntegerField(blank=True, null=True, verbose_name=_("بهای‌واحد عملیات اجرای"))

    def __str__(self):
        return f'{self.machinery_name}{self.uint}'

    class Meta:
        verbose_name = _("هزینه عملیات اجرایی")
        verbose_name_plural = _("هزینه‌های عملیات اجرایی ")


class PriceList(BaseModel):
    chapter_number = models.CharField(max_length=250, blank=True, null=True, verbose_name=_("شماره فصل"))
    item_number = models.IntegerField(blank=True, null=True, verbose_name=_("شماره آيتم"))
    description = models.CharField(max_length=250, blank=True, null=True, verbose_name=_("شرح"))
    unit = models.CharField(max_length=250, blank=True, null=True, verbose_name=_("واحد"))
    amounts = models.IntegerField(blank=True, null=True, verbose_name=_("بهاي واحد (ریال)"))

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = _("فهرست بها")
        verbose_name_plural = _("فهرست بها ")
