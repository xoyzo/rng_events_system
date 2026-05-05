from django.db import models
from bd_models.models import Special, Regime, Ball


class RNGEvent(models.Model):

    EVENT_TYPES = [
        ("global", "Global"),
        ("collectible", "Collectible"),
        ("special", "Special"),
        ("regime", "Regime"),
        ("shiny", "Shiny"),
    ]

    name = models.CharField(max_length=64)
    description = models.TextField(blank=True)

    event_type = models.CharField(max_length=32, choices=EVENT_TYPES)
    multiplier = models.FloatField(default=1.0)

    collectible_id = models.IntegerField(null=True, blank=True)
    special = models.ForeignKey(Special, null=True, blank=True, on_delete=models.CASCADE)
    regime = models.ForeignKey(Regime, null=True, blank=True, on_delete=models.CASCADE)

    global_event = models.BooleanField(default=True)
    guild_id = models.BigIntegerField(null=True, blank=True)
    local_spawn_boost = models.BooleanField(default=False)

    active = models.BooleanField(default=False)

    start_datetime = models.DateTimeField(null=True, blank=True)
    end_datetime = models.DateTimeField(null=True, blank=True)

    recurring = models.BooleanField(default=False)
    recurrence_interval_hours = models.IntegerField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
