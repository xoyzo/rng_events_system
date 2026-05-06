from discord.ext import commands
from .models import RNGEvent


class RNGEventsCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def eventstatus(self, ctx):
        events = RNGEvent.objects.filter(active=True)

        msg = "**Active RNG Events:**\n"
        for e in events:
            msg += f"- {e.name} ({e.category}) x{e.multiplier}\n"

        await ctx.send(msg)
