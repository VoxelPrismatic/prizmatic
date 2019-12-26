from ..ClsUtil import from_ts
from ..Perms import Perms, Overwrites
from ..Member import User
from ..PrizmCls import PrizmList
from ..Role import Role
from ..Raw import Raw, RawObj, RawList, RawFile

__all__ = ["Category"]

class Category:
    """
    {{cls}} instance = Category()

    {{desc}} Represents a category channel

    {{note}} This class doesn't actually exist yet
    """
    def __init__(self, *, permission_overwrites, name, parent_id, nsfw,
                 guild_id, type, id):
        self.overwrites = Overwrites(**permission_overwrites)
