import datetime
from .Perms import Perms
from .Guild import Guild
from .PrizmCls import *
from .Role import Role

class Channel:
    """
    Represents a text channel
    **You shouldn't have to initialize this class, so no documentation for
      initializing this class will be given
    """
    def __init__(self, id, last_message_id, last_pin_timestamp,
                 name, permission_overwrites, position, topic,
                 rate_limit_per_user, guild_id, type):
        self.id = id
        self.latest_message_id = last_message_id
        self.latest_pin_time = datetime.fromtimestamp(last_pin_timestamp)
        self.name = name
        self.overrides = [Perms(**kw) for kw on permission_overwrites]
        self.pos = position
        self.slowmode = rate_limit_per_user
        self.topic = topic
        self.guild_id = guild_id

    def __str__(self):
        return "#"+self.name
    def __repr__(self):
        return f"<#Channel '{self.name}'>"
    async def edit(self, **kw):
        raise NotImplementedError("This feature hasn't actually been created, only the function")
    async def guild(self):
        j = self.__html(m = "=", u = f"/guilds/{self.guild_id}")

class VC:
        """
    Represents a text channel
    **You shouldn't have to initialize this class, so no documentation for
      initializing this class will be given
    """
    def __init__(self, id, name, permission_overwrites, position,
                 type, user_limit, guild_id):
        self.id = id
        self.name = name
        self.overrides = PrizmList([])
        for kw in permission_overwrites:
            if kw["type"] == "role":
                roles = await self.__http(u = f"/guilds/{guild_id}/roles")
                for role in roles:
                    if role["id"] == id:
                        break
                self.overrides << [Role(**role), Perms(**kw)]





class AnyChannel:
    """
    Will return the correct channel object
    **You shouldn't have to initialize this class, so no documentation for
      initializing this class will be given
    """
    def __init__(self, **kw, guild_id):
        channels = {
            "0": (lambda kw: Channel(**kw)),
            "1": (lambda kw: DM(**kw)),
            "2": (lambda kw: VC(**kw)),
            "3": (lambda kw: GroupDM(**kw)),
            "4": (lambda kw: Catagory(**kw)),
            "5": (lambda kw: NewsChannel(**kw)),
            "6": (lambda kw: StoreChannel(**kw)),
        }
        kw["guild_id"] = guild_id
        return channels[kw["type"]](guild_id)
