from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class MainConfig(AppConfig):
    name = 'website_v2.main'
    verbose_name = _("Main")

    def ready(self):
        try:
            pass
        except ImportError:
            pass