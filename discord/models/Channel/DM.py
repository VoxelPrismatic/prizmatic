from ..ClsUtil import from_ts
from ..Perms import Perms, Overwrite
from ..Member import User
from ..PrizmCls import PrizmList
from ..Role import Role
from ..Raw import Raw, RawObj, RawList, RawFile

__all__ = ["DM"]

class DM:
    """
    DESCRIPTION ---
        Represents a dm channel

    PARAMS ---
        This class shouldn't be initialized by hand. Don't do that.

    FUNCTIONS ---
        None yet
    """
    def __init__(self, *, last_message_id, type, id, recipients):
        pass
