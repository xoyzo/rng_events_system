from asgiref.sync import sync_to_async
from .models import RNGEvent


class EventEngine:
    def __init__(self, bot):
        self.bot = bot

    @sync_to_async
    def get_active_events(self, category=None):
        qs = RNGEvent.objects.filter(active=True)
        if category:
            qs = qs.filter(category=category)
        return list(qs)

    async def apply_event_modifiers(self, base_value: float, category=None):
        events = await self.get_active_events(category=category)

        modifier = 1.0

        for event in events:
            modifier *= event.multiplier

        return base_value * modifier
