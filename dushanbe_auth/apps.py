from django.apps import AppConfig


class DushanbeAuthConfig(AppConfig):
    name = 'dushanbe_auth'

    def ready(self):
        from dushanbe_auth.signals import signals
