from django.apps import AppConfig as BaseAppConfig
from django.utils.translation import gettext_lazy as _


class MessagesDrfConfig(BaseAppConfig):
    name = "messaging"
    label = "messaging"
    verbose_name = _("messaging")
