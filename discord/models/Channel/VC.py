import datetime
from ..Perms import Perms
from ..Guild import Guild
from ..User import User
from ..PrizmCls import PrizmList
from ..Role import Role
from ..Raw import Raw, RawObj, RawList, RawFile
from ..Overwrite import Overwrite

class VC:
    """
    DESCRIPTION ---
        Represents a voice channel
        
    PARAMS ---
        This class shouldn't be initialized by hand. Don't do that.
        
    FUNCTIONS ---
        None yet
    """
    def __init__(self, id, name, permission_overwrites, position,
                 type, user_limit, guild_id, bot):
        self.id = id
        self.name = name
        self.overrides = PrizmList([])
        self.bot = bot