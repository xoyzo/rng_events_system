async def broadcast_all(bot, message: str):

    for guild in bot.guilds:
        try:
            channel = guild.system_channel or next(
                (c for c in guild.text_channels if c.permissions_for(guild.me).send_messages),
                None
            )

            if channel:
                await channel.send(message)
        except Exception:
            pass
