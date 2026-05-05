from .engine import get_modifiers


async def modify_spawn(ball, base_rate=1.0, regime=None, special=None, guild_id=None):

    mods = await get_modifiers(
        ball=ball,
        regime=regime,
        special=special,
        guild_id=guild_id
    )

    return (
        base_rate
        * mods["global"]
        * mods["collectible"]
        * mods["special"]
        * mods["regime"]
    )
