from django.db import models

from collect.models import Collectible

from bd_models.models import (
    Regime,
    Special,
    Economy
)


class RNGEvent(models.Model):

    target_collectible = models.ForeignKey(
        Collectible,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="rng_events"
    )

    target_regime = models.ForeignKey(
        Regime,
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )

    target_special = models.ForeignKey(
        Special,
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )

    target_economy = models.ForeignKey(
        Economy,
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )
