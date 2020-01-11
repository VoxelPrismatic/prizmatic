from ..Guild import Guild

__all__ = ["OfflineGuild"]

class OfflineGuild(Guild):
    """
    {{cls}} instance = OfflineGuild()

    {{desc}} Represents a guild, thats offline

    {{note}} Documentation for this class is not complete yet
    """
    def __init__(self, **kw):
        if kw:
            print(
                "Error: Class 'Ban' has extra kwargs added by the gateway"
            )
            print(kw)
            exit()
