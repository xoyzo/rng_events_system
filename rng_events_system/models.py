from django.db import models
from bd_models.models import Regime, Special
from collect.models import Collectible


class RNGEvent(models.Model):
    CATEGORY_CHOICES = [
        ("spawn", "Spawn"),
        ("economy", "Economy"),
        ("regime", "Regime"),
        ("special", "Special"),
    ]

    SCOPE_CHOICES = [
        ("local", "Local"),
        ("global", "Global"),
        ("whitelist", "Whitelist"),
    ]

    name = models.CharField(max_length=100, unique=True)

    # NEW: fully editable Discord message template
    message = models.TextField(
        default="⚡ {event_name} is active!",
        help_text="Message sent when event triggers. Supports {event_name}, {multiplier}, etc."
    )

    description = models.TextField(blank=True)

    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    scope = models.CharField(max_length=20, choices=SCOPE_CHOICES, default="local")

    collectible = models.ForeignKey(Collectible, null=True, blank=True, on_delete=models.CASCADE)
    regime = models.ForeignKey(Regime, null=True, blank=True, on_delete=models.CASCADE)
    special = models.ForeignKey(Special, null=True, blank=True, on_delete=models.CASCADE)

    multiplier = models.FloatField(default=1.0)

    active = models.BooleanField(default=False)

    start_datetime = models.DateTimeField(null=True, blank=True)
    end_datetime = models.DateTimeField(null=True, blank=True)

    recurring = models.BooleanField(default=False)
    recurrence_interval_hours = models.IntegerField(null=True, blank=True)

    announce = models.BooleanField(default=True)

    # NEW: allows admin to force test events instantly
    test_run = models.BooleanField(
        default=False,
        help_text="If enabled, event can be manually triggered for testing"
    )

    def __str__(self):
        return f"{self.name} ({self.category})"
