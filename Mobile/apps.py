from django.apps import AppConfig


class MobileConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Mobile'



    def ready(self):
        import Mobile.signals