from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ImplementationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'implementation'
    verbose_name = _("عملیات اجرایی")
