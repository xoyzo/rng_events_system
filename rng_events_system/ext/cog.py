from discord.ext import commands
from discord import app_commands

from rng_events_system.models import RNGEvent


class RNGCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    @app_commands.command()
    async def rng_list(self, interaction):

        events = []

        async for event in RNGEvent.objects.all():
            events.append(event.name)

        await interaction.response.send_message(
            "\n".join(events),
            ephemeral=True
        )
