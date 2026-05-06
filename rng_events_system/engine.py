import asyncio
from .models import RNGEvent


class EventEngine:
    def __init__(self, bot):
        self.bot = bot

    async def get_active_events(self):
        return RNGEvent.objects.filter(active=True)

    async def apply_event_modifiers(self, base_value: float):
        events = await self.get_active_events()

        modifier = 1.0

        async for event in events:
            modifier *= event.multiplier

        return base_value * modifier
