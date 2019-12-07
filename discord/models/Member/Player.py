from .User import User
from .. import PrizmCls
from ..Raw import RawObjs
from ..Role import Role

__all__ = ["Player"]

class Player:
    """
    Represents a player [or member] in a guild
    """
    def __init__(self, deaf: bool, hoisted_role: str, joined: str,
                 mute: bool, nick, premium_since: str, roles: list,
                 user: dict, bot_obj):
        self.user = super().__init__(**user)
        self.vc = {
            "deaf": deaf,
            "mute": mute,
        }
        self.nick = nick
        self.boosted_at: premium_since

        self.roles = RawObjs(Role, roles, bot_obj = bot_obj)
        self.bot_obj = bot_obj
