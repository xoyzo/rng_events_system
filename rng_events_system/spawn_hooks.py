from asgiref.sync import sync_to_async
from .models import RNGEvent


@sync_to_async
def get_spawn_events():
    return list(
        RNGEvent.objects.filter(active=True, category="spawn")
    )


async def apply_spawn_modifiers(base_chance: float) -> float:
    events = await get_spawn_events()

    modifier = 1.0

    for event in events:
        modifier *= event.multiplier

    return base_chance * modifier
