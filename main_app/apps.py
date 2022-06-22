from django.apps import AppConfig


class MainAppConfig(AppConfig):
    name = 'main_app'

    def ready(self):
        from . import views
        views.start()

        