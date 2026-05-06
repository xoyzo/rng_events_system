from django.apps import AppConfig


class RngEventsSystemConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "rng_events_system"

    def ready(self):
        import rng_events_system.spawn_hooks  # ensures hooks load
