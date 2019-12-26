from ..ClsUtil import from_ts
from ..Perms import Perms, Overwrite
from ..Member import User
from ..PrizmCls import PrizmList
from ..Role import Role
from ..Raw import Raw, RawObj, RawList, RawFile

__all__ = ["DM"]

class DM:
    """
    {{cls}} instance = DM(*, last_message_id, type, id, recipients, bot_obj)

    {{desc}} Represents a dm channel

    {{note}} This class shouldn't be initialized by hand. Don't do that.

    {{param}} last_message_id
    """
    def __init__(self, *, last_message_id, type, id, recipients, bot_obj):
        self.latest_message_id = int(last_message_id)
        self.type = type
        self.id = int(id)
        #self.users =
