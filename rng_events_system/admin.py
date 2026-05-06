from django.contrib import admin

from .models import RNGEvent


@admin.register(RNGEvent)
class RNGEventAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "scope",
        "multiplier",
        "active",
        "trigger_source",
    )

    list_filter = (
        "scope",
        "active",
        "trigger_source",
        "target_collectible",
        "target_regime",
        "target_special",
        "target_economy",
    )

    autocomplete_fields = (
        "target_collectible",
        "target_regime",
        "target_special",
        "target_economy",
    )

    search_fields = (
        "name",
    )
