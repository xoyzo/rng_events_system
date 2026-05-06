class EventAnnouncer:

    @staticmethod
    def format_message(event):
        return event.message.format(
            event_name=event.name,
            multiplier=event.multiplier,
            category=event.category
        )
