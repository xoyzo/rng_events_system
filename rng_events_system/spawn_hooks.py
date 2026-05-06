from .models import RNGEvent


async def apply_spawn_modifiers(base_chance: float) -> float:
    events = RNGEvent.objects.filter(active=True, category="spawn")

    modifier = 1.0

    for event in events:
        modifier *= event.multiplier

    return base_chance * modifier
