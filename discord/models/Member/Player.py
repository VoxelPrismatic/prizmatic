from .User import User
from .. import PrizmCls
from ..Raw import RawObjs
from ..Role import Role
from ..ClsUtil import from_ts

__all__ = ["Player"]

class Player(User):
    """
    Represents a player [or member] in a guild
    """
    def __init__(self, *, deaf: bool, hoisted_role = False, joined_at = "",
                 mute = False, nick = "", premium_since = None, roles = [],
                 user = {}, guild_id = 0, bot_obj = None):
        self.user = bot_obj.raw("users", user, bot_obj = bot_obj)[0]
        self.vc = {
            "deaf": deaf,
            "mute": mute
        }
        self.nick = nick
        self.boosted_at = premium_since

        self.roles = [bot_obj.roles(role) for role in roles]
        self.hoisted = hoisted_role
        self.joined = from_ts(joined_at)
        self.guild_id = int(guild_id)
        self.bot_obj = bot_obj

    @property
    def id(self):
        return self.user.id

    @property
    def discrim(self):
        return self.user.discrim

    @property
    def guild(self):
        return self.bot_obj.guilds(self.guild_id)

    @property
    def ping(self):
        return "<@" + str(self.id) + ">"
