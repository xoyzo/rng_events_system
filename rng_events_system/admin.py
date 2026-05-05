from django.contrib import admin
from .models import RNGEvent


@admin.register(RNGEvent)
class RNGEventAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "event_type",
        "multiplier",
        "active",
        "start_datetime",
        "end_datetime",
    )

    list_filter = ("active", "event_type")
    search_fields = ("name",)
