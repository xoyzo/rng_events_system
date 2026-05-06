from django.contrib import admin
from .models import RNGEvent
from collect.models import Collectible
from bd_models.models import Regime, Special


# =========================
# INLINE: makes editing clean
# =========================

class CollectibleInline(admin.TabularInline):
    model = RNGEvent
    extra = 0
    fields = ["collectible", "multiplier"]
    autocomplete_fields = ["collectible"]
    verbose_name = "Collectible Target"
    verbose_name_plural = "Collectible Targets"


# =========================
# MAIN EVENT ADMIN
# =========================

@admin.register(RNGEvent)
class RNGEventAdmin(admin.ModelAdmin):

    # ---------- LIST VIEW ----------
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

    list_editable = [
        "active",
        "announce",
    ]

    list_filter = [
        "category",
        "scope",
        "active",
        "announce",
        "recurring",
    ]

    search_fields = [
        "name",
        "description",
        "collectible__name",
        "regime__name",
        "special__name",
    ]

    ordering = ["-active", "name"]

    # ---------- SPEED BOOST ----------
    autocomplete_fields = [
        "collectible",
        "regime",
        "special",
    ]

    # ---------- FIELD LAYOUT ----------
    fieldsets = (
        ("🧠 Basic Info", {
            "fields": (
                "name",
                "description",
                "active",
                "announce",
            )
        }),

        ("🎯 Event Type", {
            "fields": (
                "category",
                "scope",
            )
        }),

        ("⚙️ Targets (optional)", {
            "fields": (
                "collectible",
                "regime",
                "special",
            )
        }),

        ("📊 Effects", {
            "fields": (
                "multiplier",
            )
        }),

        ("⏰ Scheduling", {
            "fields": (
                "start_datetime",
                "end_datetime",
                "recurring",
                "recurrence_interval_hours",
            )
        }),
    )

    # ---------- READABLE LABELS ----------
    @admin.display(description="Event Status")
    def event_status(self, obj):
        if obj.active:
            return "🟢 Active"
        return "🔴 Inactive"


# =========================
# OPTIONAL: READ-ONLY VIEW (DEBUG STYLE)
# =========================

@admin.register(Collectible)
class CollectibleAdmin(admin.ModelAdmin):

    list_display = [
        "name",
        "emoji",
        "cost",
    ]

    search_fields = ["name"]
