from discord.ext import commands
from discord import app_commands
import discord

from rng_events_system.models import RNGEvent
from rng_events_system.scheduler import scheduler_loop


class RNGCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.task = None

    async def cog_load(self):
        self.task = self.bot.loop.create_task(scheduler_loop(self.bot))

    @app_commands.command(name="rng_list")
    async def rng_list(self, interaction: discord.Interaction):

        events = RNGEvent.objects.all()
        text = "🎲 Active Events:\n"

        async for e in events:
            text += f"- {e.name} | active={e.active}\n"

        await interaction.response.send_message(text, ephemeral=True)

    @app_commands.command(name="rng_start")
    async def rng_start(self, interaction: discord.Interaction, event_id: int):

        e = await RNGEvent.objects.aget(id=event_id)
        e.active = True
        await e.asave()

        await interaction.response.send_message("Started ✔️", ephemeral=True)

    @app_commands.command(name="rng_stop")
    async def rng_stop(self, interaction: discord.Interaction, event_id: int):

        e = await RNGEvent.objects.aget(id=event_id)
        e.active = False
        await e.asave()

        await interaction.response.send_message("Stopped ✔️", ephemeral=True)


async def setup(bot):
    await bot.add_cog(RNGCog(bot))
