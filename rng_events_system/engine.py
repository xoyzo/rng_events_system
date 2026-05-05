from .models import RNGEvent


async def get_modifiers(ball=None, special=None, regime=None, guild_id=None):

    events = RNGEvent.objects.filter(active=True)

    mods = {
        "global": 1.0,
        "collectible": 1.0,
        "special": 1.0,
        "regime": 1.0,
        "shiny": 1.0,
    }

    async for e in events:

        if e.event_type == "global":
            mods["global"] *= e.multiplier

        if e.event_type == "collectible" and ball and e.collectible_id == ball.id:
            mods["collectible"] *= e.multiplier

        if e.event_type == "special" and special and e.special_id == special.id:
            mods["special"] *= e.multiplier

        if e.event_type == "regime" and regime and e.regime_id == regime.id:
            mods["regime"] *= e.multiplier

        if e.event_type == "shiny":
            mods["shiny"] *= e.multiplier

    return mods
