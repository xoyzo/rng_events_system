from django.db import migrations, models


def create_default_events(apps, schema_editor):

    RNGEvent = apps.get_model(
        "rng_events_system",
        "RNGEvent"
    )

    if not RNGEvent.objects.exists():

        RNGEvent.objects.create(
            name="Double Spawn Hour",
            category="spawn",
            scope="global",
            multiplier=2.0,
            duration_minutes=60,
            announcement_text="Spawn rates doubled."
        )

        RNGEvent.objects.create(
            name="Economic Surge",
            category="economy",
            scope="local",
            multiplier=1.5,
            duration_minutes=120,
            announcement_text="Economy boosted."
        )


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        (
            "bd_models",
            "0014_alter_ball_options_alter_ballinstance_options_and_more"
        ),
    ]

    operations = [

        migrations.CreateModel(
            name="RNGEvent",
            fields=[
                ("id", models.BigAutoField(
                    auto_created=True,
                    primary_key=True,
                    serialize=False,
                    verbose_name="ID"
                )),
                ("name", models.CharField(
                    max_length=50,
                    unique=True
                )),
                ("category", models.CharField(
                    max_length=20
                )),
                ("scope", models.CharField(
                    max_length=20
                )),
                ("multiplier", models.FloatField(
                    default=1.0
                )),
                ("duration_minutes", models.IntegerField(
                    default=60
                )),
                ("active", models.BooleanField(
                    default=False
                )),
            ],
        ),

        migrations.RunPython(
            create_default_events
        ),

    ]
