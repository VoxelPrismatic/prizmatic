from .Perms import Perms
from ..Snow import Snow

__all__ = ["Overwrite"]

class Overwrite:
    """
    {{cls}} instance = Overwrite(*, id, type, allow_int, deny_int, bot_obj)

    {{desc}} Represents a permission overwrite

    {{param}} id [int, ~/Snow, str]
        The ID of the overwrited object, eg the role or user ID

    {{param}} type [str]
        Either "role" or "member"

    {{param}} allow [int]
        The allowed permissions integer

    {{param}} deny [int]
        The denied permissions integer

    {{param}} bot_obj [~/Bot]
        The bot object

    {{prop}} empty [bool]
        Whether or not this overwrite does anything

    {{prop}} id [int]
        Target ID

    {{prop}} type [str]
        Either "role" or "member"

    {{prop} perms [~/Perms.Perms]
        The permissions object

    {{prop}} bot_obj [~/Bot, None]
        The bot object, or None

    {{prop}} target [Any[~/Role, ~/Member.User]]
        The target object, will throw an `AttributeError` if bot_obj is None
    """
    def __init__(self, *, id, type, allow, deny, bot_obj = None):
        self.id = int(id)
        self.type = type
        self.perms = Perms(allow = allow, deny = deny)
        self.bot_obj = bot_obj

    @property
    def target(self):
        if self.type == "role":
            return self.bot_obj.roles(self.id)
        if self.type == "member":
            return self.bot_obj.users(self.id)

    @property
    def empty(self) -> bool:
        return self.perms.empty

    def update(self, allow: int = None, deny: int = None):
        if allow is None:
            allow_int = self.perms.allow_int
        if deny is None:
            deny_int = self.perms.deny_int
        self.perms.update_int(allow = allow_int, deny = deny_int)

    def __dict__(self):
        """
        {{bltin}} instance.__dict__()
        {{usage}} dict(instance)

        {{pydesc}} __dict__

        {{rtn}} [dict]
        """
        return {
            "id": str(self.id),
            "type": self.type,
            "allow": self.perms.allow_int,
            "deny": self.perms.deny_int
        }
