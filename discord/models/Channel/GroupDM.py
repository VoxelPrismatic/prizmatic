from ..Role import Role
from ..Member import User
from ..PrizmCls import PrizmList
from ..Perms import Perms, Overwrite
from ..ClsUtil import from_ts, extra_kw
from ..Raw import Raw, RawObj, RawList, RawFile

__all__ = ["GroupDM"]

class GroupDM:
    """
    {{cls}} instance = GroupDM()

    {{desc}} Represents a Group DM

    {{noexist}}
    """
    def __init__(self, **kw):
        extra_kw(kw, "GroupDM")
