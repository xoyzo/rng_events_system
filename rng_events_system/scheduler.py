import asyncio
from django.utils import timezone
from .models import RNGEvent
from .announcer import broadcast_all


async def scheduler_loop(bot):

    while True:
        now = timezone.now()

        events = RNGEvent.objects.all()

        async for e in events:

            # start
            if e.start_datetime and not e.active:
                if now >= e.start_datetime:
                    e.active = True
                    await e.asave()
                    await broadcast_all(bot, f"🎉 Event Started: {e.name}")

            # end
            if e.end_datetime and e.active:
                if now >= e.end_datetime:
                    e.active = False
                    await e.asave()
                    await broadcast_all(bot, f"⛔ Event Ended: {e.name}")

                    # recurrence
                    if e.recurring and e.recurrence_interval_hours:
                        e.start_datetime = now + timezone.timedelta(
                            hours=e.recurrence_interval_hours
                        )
                        e.end_datetime = None
                        await e.asave()

        await asyncio.sleep(30)
