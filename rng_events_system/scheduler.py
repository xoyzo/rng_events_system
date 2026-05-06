import asyncio
from django.utils import timezone
from .models import RNGEvent


async def scheduler_loop():

    while True:

        now = timezone.now()

        events = RNGEvent.objects.all()

        async for event in events:

            if event.start_datetime and not event.active:
                if now >= event.start_datetime:
                    event.active = True
                    await event.asave()

            if event.end_datetime and event.active:
                if now >= event.end_datetime:
                    event.active = False
                    await event.asave()

        await asyncio.sleep(30)
