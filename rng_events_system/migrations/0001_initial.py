from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("bd_models", "0014_alter_ball_options_alter_ballinstance_options_and_more"),
        ("collect", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="RNGEvent",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=100,
                        unique=True,
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True,
                        help_text="Internal description for admins.",
                    ),
                ),
                (
                    "message",
                    models.TextField(
                        default="⚡ {event_name} is active!",
                        help_text=(
                            "Message broadcasted when event triggers. "
                            "Supports variables: {event_name}, {multiplier}, {category}"
                        ),
                    ),
                ),
                (
                    "category",
                    models.CharField(
                        max_length=20,
                        choices=[
                            ("spawn", "Spawn"),
                            ("economy", "Economy"),
                            ("regime", "Regime"),
                            ("special", "Special"),
                        ],
                    ),
                ),
                (
                    "scope",
                    models.CharField(
                        max_length=20,
                        choices=[
                            ("local", "Local"),
                            ("global", "Global"),
                            ("whitelist", "Whitelist"),
                        ],
                        default="local",
                    ),
                ),
                (
                    "collectible",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="collect.collectible",
                        related_name="rng_events",
                        help_text="Optional collectible affected by this event.",
                    ),
                ),
                (
                    "regime",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="bd_models.regime",
                        related_name="rng_events",
                        help_text="Optional regime affected by this event.",
                    ),
                ),
                (
                    "special",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="bd_models.special",
                        related_name="rng_events",
                        help_text="Optional special affected by this event.",
                    ),
                ),
                (
                    "multiplier",
                    models.FloatField(
                        default=1.0,
                        help_text="Global modifier applied by this event.",
                    ),
                ),
                (
                    "active",
                    models.BooleanField(
                        default=False,
                        help_text="Whether this event is currently active.",
                    ),
                ),
                (
                    "start_datetime",
                    models.DateTimeField(
                        blank=True,
                        null=True,
                    ),
                ),
                (
                    "end_datetime",
                    models.DateTimeField(
                        blank=True,
                        null=True,
                    ),
                ),
                (
                    "recurring",
                    models.BooleanField(
                        default=False,
                    ),
                ),
                (
                    "recurrence_interval_hours",
                    models.IntegerField(
                        blank=True,
                        null=True,
                        help_text="If recurring, interval in hours.",
                    ),
                ),
                (
                    "announce",
                    models.BooleanField(
                        default=True,
                        help_text="Whether this event is broadcast to Discord.",
                    ),
                ),
                (
                    "test_run",
                    models.BooleanField(
                        default=False,
                        help_text="Allows manual triggering from admin for testing.",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True,
                    ),
                ),
            ],
            options={
                "verbose_name": "RNG Event",
                "verbose_name_plural": "RNG Events",
                "ordering": ["-active", "name"],
            },
        ),
    ]
