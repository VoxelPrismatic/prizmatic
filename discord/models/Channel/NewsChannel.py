from ..ClsUtil import from_ts
from ..Perms import Perms, Overwrites
from ..Member import User
from ..PrizmCls import PrizmList
from ..Role import Role
from ..Raw import Raw, RawObj, RawList, RawFile

__all__ = ["NewsChannel"]

class NewsChannel:
    """
    DESCRIPTION ---
        Represents a news/announcements channel

    PARAMS ---
        This class shouldn't be initialized by hand. Don't do that.

    FUNCTIONS ---
        None yet
    """
    def __init__(self, *, id, guild_id, name, type, position,
                 permission_overwrites, rate_limit_per_user, nsfw, topic,
                 last_message_id, parent_id = None, last_pin_timestamp, bot_obj):
        self.id = id
        self.latest_message_id = last_message_id
        self.latest_pin_time = from_ts(last_pin_timestamp)
        self.name = name
        self.overwrites = Overwrites(**permission_overwrites)
        self.pos = position
        self.slowmode = rate_limit_per_user
        self.topic = topic
        self.guild_id = guild_id
        self.guild = bot_obj.listener.guilds(guild_id)
        self.catagory_id = parent_id
        self.bot_obj = bot_obj

    def __str__(self):
        return "#" + self.name

    @property
    def ping(self):
        return f"<#{self.id}>"

    def __repr__(self):
        return f"<#NewsChannel '{self.name}'>"

    async def edit(self, **kw):
        raise NotImplementedError(
            "This feature hasn't actually been created, only the function"
        )

    async def load(self):
        await self.guild.make()

    async def update(self):
        raise NotImplementedError(
            "This feature hasn't actually been created, only the function"
        )
