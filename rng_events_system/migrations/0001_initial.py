from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("bd_models", "0014_alter_ball_options_alter_ballinstance_options_and_more"),
    ]

    operations = [

        # =========================
        # 🎲 MAIN EVENT TABLE
        # =========================
        migrations.CreateModel(
            name="RNGEvent",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),

                # Basic info
                ("name", models.CharField(max_length=100, unique=True)),
                ("enabled", models.BooleanField(default=True)),
                ("active", models.BooleanField(default=False)),

                # Category system
                ("category", models.CharField(
                    max_length=20,
                    choices=[
                        ("spawn", "Spawn"),
                        ("economy", "Economy"),
                        ("regime", "Regime"),
                        ("special", "Special"),
                    ],
                )),

                # Scope system
                ("scope", models.CharField(
                    max_length=20,
                    choices=[
                        ("local", "Local"),
                        ("global", "Global"),
                        ("whitelist", "Whitelist"),
                    ],
                    default="local",
                )),

                # Effects
                ("multiplier", models.FloatField(default=1.0)),

                # Scheduling
                ("start_datetime", models.DateTimeField(null=True, blank=True)),
                ("end_datetime", models.DateTimeField(null=True, blank=True)),
                ("recurring", models.BooleanField(default=False)),
                ("recurrence_hours", models.IntegerField(null=True, blank=True)),

                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),


        # =========================
        # 📣 EVENT MESSAGE TEMPLATE
        # =========================
        migrations.CreateModel(
            name="RNGEventMessage",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),

                # Link to event
                ("event", models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    related_name="messages",
                    to="rng_events_system.rngevent",
                )),

                # Message system
                ("title", models.CharField(max_length=120)),
                ("description", models.TextField(blank=True)),

                # Embed customization
                ("embed_title", models.CharField(max_length=120, blank=True)),
                ("embed_body", models.TextField(blank=True)),
                ("embed_color", models.CharField(
                    max_length=7,
                    default="#00ffcc",
                    help_text="Hex color"
                )),

                # Behavior
                ("channel_id", models.BigIntegerField(null=True, blank=True)),
                ("ping_everyone", models.BooleanField(default=False)),

                # Placeholder system (IMPORTANT)
                ("use_placeholders", models.BooleanField(default=True)),
            ],
        ),


        # =========================
        # 🌍 EVENT WHITELIST SERVERS
        # =========================
        migrations.CreateModel(
            name="RNGEventWhitelist",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),

                ("event", models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    to="rng_events_system.rngevent",
                    related_name="whitelist",
                )),

                ("guild_id", models.BigIntegerField()),
            ],
        ),
    ]
