from django.contrib import admin
from .models import RNGEvent


@admin.register(RNGEvent)
class RNGEventAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "category",
        "scope",
        "multiplier",
        "active",
        "announce",
        "start_datetime",
        "end_datetime",
    ]

    list_editable = ["active", "announce", "multiplier"]

    list_filter = ["active", "category", "scope", "announce"]

    search_fields = ["name", "description", "message"]

    ordering = ["-active", "name"]

    fieldsets = (
        ("Core Event Info", {
            "fields": ("name", "description", "message", "category", "scope")
        }),
        ("Targets", {
            "fields": ("collectible", "regime", "special")
        }),
        ("Balance", {
            "fields": ("multiplier",)
        }),
        ("Timing", {
            "fields": ("active", "start_datetime", "end_datetime", "recurring", "recurrence_interval_hours")
        }),
        ("Controls", {
            "fields": ("announce", "test_run")
        }),
    )
