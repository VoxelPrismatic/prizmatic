from ..Member import User
from ..ClsUtil import from_ts, extra_kw

__all__ = ["InviteMetadata"]

class InviteMetadata:
    """
    {{cls}} instance = InviteMetadata(*, too_many_args_to_list_here)

    {{desc}} Represents invite metadata

    {{param}} inviter [dict]
        The user that created the invite

    {{param}} uses [int]
        The number of uses

    {{param}} max_uses [int]
        The max number of uses, 0 being an infinite amount

    {{param}} max_age [int]
        The max age in days, 0 being never

    {{param}} temporary [bool]
        If there is a max_age of a max_uses

    {{param}} created_at [datetime.datetime, str]
        The created at timestamp

    {{param}} bot_obj [~/Bot]
        The bot object

    {{prop}} inviter [~/Member.User]
        The user that created the invite

    {{prop}} uses [int]
        The number of uses

    {{prop}} max_uses [int]
        The max number of uses, 0 being an infinite amount

    {{prop}} max_age [int]
        The max age in days, 0 being never

    {{prop}} temporary [bool]
        If there is a max_age of a max_uses

    {{prop}} made_at [datetime.datetime]
        The created at timestamp

    {{prop}} bot_obj [~/Bot]
        The bot object
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
        self.bot_obj = bot_obj
