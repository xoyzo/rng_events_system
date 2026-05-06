from django.contrib import admin
from .models import RNGEvent


@admin.register(RNGEvent)
class RNGEventAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "category",
        "scope",
        "multiplier",
        "active",
        "start_datetime",
        "end_datetime"
    )

    list_filter = (
        "category",
        "scope",
        "active"
    )

    search_fields = (
        "name",
    )

    fieldsets = (
        ("Basic", {
            "fields": (
                "name",
                "description",
                "active"
            )
        }),

        ("Event Type", {
            "fields": (
                "category",
                "scope"
            )
        }),

        ("Targets", {
            "fields": (
                "collectible",
                "regime",
                "special"
            )
        }),

        ("Effects", {
            "fields": (
                "multiplier",
            )
        }),

        ("Schedule", {
            "fields": (
                "start_datetime",
                "end_datetime",
                "recurring",
                "recurrence_interval_hours"
            )
        }),

        ("Broadcast", {
            "fields": (
                "announce",
            )
        }),
    )
