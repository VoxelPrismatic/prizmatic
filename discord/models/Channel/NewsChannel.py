from ..ClsUtil import from_ts
from ..Perms import Perms, Overwrites
from ..Member import User
from ..PrizmCls import PrizmList
from ..Role import Role
from ..Raw import Raw, RawObj, RawList, RawFile
from .Channel import Channel

__all__ = ["NewsChannel"]

class NewsChannel(Channel):
    """
    {{subcls}} [~.Channel] instance = NewsChannel(*, too_many_args_to_list_here)

    {{desc}} Represents a NewsChannel

    {{noinit}}

    {{note}} All the params and props are the same as in ~.Channel
    """
    def __init__(self, *, id, guild_id, name, type, position,
                 permission_overwrites, rate_limit_per_user, nsfw, topic,
                 last_message_id, parent_id = None, last_pin_timestamp,
                 bot_obj = None, **kw):
        if kw:
            print(
                "Error: Class 'NewsChannel' has extra kwargs added by the"
                "gateway"
            )
            print(kw)
            exit()
        super().__init__(
            id = id, guild_id = guild_id, name = name, type = type,
            position = position, permission_overwrites = permission_overwrites,
            rate_limit_per_user = rate_limit_per_user, nsfw = nsfw,
            topic = topic, last_message_id = last_message_id, bot_obj = bot_obj,
            last_pin_timestamp = last_pin_timestamp
        )
