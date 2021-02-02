from django.apps import AppConfig


class DushanbeConfig(AppConfig):
    name = 'dushanbe'

    def ready(self):
        from dushanbe.signals import signals


