from ..Role import Role
from ..Member import User
from ..PrizmCls import PrizmList
from ..Perms import Perms, Overwrite
from ..ClsUtil import from_ts, extra_kw
from ..Raw import Raw, RawObj, RawList, RawFile

__all__ = ["DM"]

class DM:
    """
    {{cls}} instance = DM(*, last_message_id, type, id, recipients, bot_obj)

    {{desc}} Represents a dm channel

    {{noinit}}

    {{note}} The documentation for this class is not complete yet

    {{param}} last_message_id []
    """
    def __init__(self, *, last_message_id, type, id, recipients, bot_obj, **kw):
        extra_kw(kw, "DM")
        self.latest_message_id = int(last_message_id)
        self.type = type
        self.id = int(id)
        self.users = bot_obj.raw("users", recipients, bot_obj = bot_obj)
