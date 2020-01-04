from ..Member import User
from ..ClsUtil import from_ts, extra_kw

__all__ = ["InviteMetadata"]

class InviteMetadata:
    """
    {{cls}} instance = InviteMetadata(*, too_many_args_to_list_here)

    {{desc}} Represents invite metadata
    """
    def __init__(self, *, inviter, uses, max_uses, max_age, temporary,
                 created_at, bot_obj = None, **kw):
        extra_kw(kw, "InviteMetadata")
        self.inviter = User(**inviter)
        self.uses = uses
        self.max_uses = max_uses
        self.max_age = max_age
        self.temp = temporary
        self.made_at = from_ts(created_at)
