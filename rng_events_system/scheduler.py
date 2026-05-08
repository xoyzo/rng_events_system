import asyncio
from django.utils import timezone
from asgiref.sync import sync_to_async
from .models import RNGEvent
from .announcer import EventAnnouncer


class EventScheduler:
    def __init__(self, bot):
        self.bot = bot

    async def run_loop(self):
        while True:
            await self.check_events()
            await asyncio.sleep(60)

    @sync_to_async
    def get_events(self):
        return list(RNGEvent.objects.all())

    @sync_to_async
    def deactivate_event(self, event):
        event.active = False
        event.save(update_fields=["active"])

    async def check_events(self):
        now = timezone.now()
        events = await self.get_events()

        for event in events:

            if event.start_datetime and event.start_datetime > now:
                continue

            if event.end_datetime and event.end_datetime < now:
                await self.deactivate_event(event)
                continue

            if event.announce:
                await self.broadcast(event)

    async def broadcast(self, event):
        msg = EventAnnouncer.format_message(event)

        for guild in self.bot.guilds:
            await self.send_to_guild(guild, msg)

    async def send_to_guild(self, guild, msg):
        for channel in guild.text_channels:
            if channel.permissions_for(guild.me).send_messages:
                await channel.send(msg)
                break
