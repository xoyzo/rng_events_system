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
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=100)),
                ("description", models.TextField(blank=True)),
                ("category", models.CharField(max_length=20)),
                ("scope", models.CharField(max_length=20)),
                ("multiplier", models.FloatField(default=1.0)),
                ("active", models.BooleanField(default=False)),
                ("start_datetime", models.DateTimeField(null=True, blank=True)),
                ("end_datetime", models.DateTimeField(null=True, blank=True)),
                ("recurring", models.BooleanField(default=False)),
                ("recurrence_interval_hours", models.IntegerField(null=True, blank=True)),
                ("announce", models.BooleanField(default=True)),
            ],
        ),
    ]
