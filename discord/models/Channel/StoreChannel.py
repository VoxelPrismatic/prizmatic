from ..ClsUtil import from_ts
from ..Perms import Perms, Overwrites
from ..Member import User
from ..PrizmCls import PrizmList
from ..Role import Role
from ..Raw import Raw, RawObj, RawList, RawFile

__all__ = ["StoreChannel"]

class StoreChannel:
    """
    DESCRIPTION ---
        Represents a store channel

    PARAMS ---
        This class shouldn't be initalized by hand. Don't do that.

    FUNCTIONS ---
        None yet
    """
    def __init__(self, *, id, guild_id, name, type, position, permission_overwrites,
                 nsfw, parent_id, bot_obj):
        self.id = int(id)
        self.guild_id = int(guild_id)
        self.guild = bot_obj.listeners.guilds(guild_id)
        self.name = name
        self.position = position
        self.nsfw = nsfw
        self.overwrites = Overwrites(**permission_overwrites)
        self.catagory_id = parent_id
        self.bot_obj = bot_obj

    #async def edit(self, *, id, catagory,: Catagory, overwrites,

    @property
    def ping(self):
        return f"<#{self.id}>"
