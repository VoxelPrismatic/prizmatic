from ..Guild import Guild

__all__ = ["OfflineGuild"]

class OfflineGuild(Guild):
    """
    DESCRIPTION ---
        Represents a guild, thats offline

    PARAMS ---
        This class shouldn't be initialized by hand. Don't do that.

    FUNCTIONS ---
        semiguild = OfflineGuild(id, unavailable)
        - Creates a new OfflineGuild object

        await semiguild.refresh()
        - Returns the guild object
        - The regular guild class has this too, but this is needed
          for anything to be useful
    """
    def __init__(self, **kw):
        if kw:
            print(
                "Error: Class 'Ban' has extra kwargs added by the gateway"
            )
            print(kw)
            exit()
