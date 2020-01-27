from ..Role import Role
from ..Member import User
from .Channel import Channel
from ..PrizmCls import PrizmList
from ..Perms import Perms, Overwrites
from ..ClsUtil import from_ts, extra_kw
from ..Raw import Raw, RawObj, RawList, RawFile

__all__ = ["StoreChannel"]

class StoreChannel(Channel):
    """
    {{subcls}} [~.Channel] instance = StoreChannel(*, too_many_args_to_list)

    {{desc}} Represents a StoreChannel

    {{noinit}}

    {{note}} All the params and props are the same as in ~.Channel

    {{notdone}}
    """
    def __init__(self, *, id, guild_id, name, type, position,
                 permission_overwrites, rate_limit_per_user, nsfw, topic,
                 last_message_id, parent_id = None, last_pin_timestamp,
                 bot_obj = None, **kw):
        extra_kw(kw, "StoreChannel")
        super().__init__(
            id = id, guild_id = guild_id, name = name, type = type,
            position = position, permission_overwrites = permission_overwrites,
            rate_limit_per_user = rate_limit_per_user, nsfw = nsfw,
            topic = topic, last_message_id = last_message_id, bot_obj = bot_obj,
            last_pin_timestamp = last_pin_timestamp
        )

    #async def edit(self, *, id, catagory,: Catagory, overwrites,

    @property
    def ping(self):
        return f"<#{self.id}>"
