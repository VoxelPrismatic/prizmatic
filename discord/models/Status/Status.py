from ..Member import User
from ..Role import Role
from ..Raw import RawObjs

class Status:
    """
    DESCRIPTION ---
        Represents a presence, or "status" as referred to in the app
        
    PARAMS ---
        This class shouldn't be initialized by hand. Don't do that.
        
    FUNCTIONS ---
        None yet
    """
    def __init__(self, user, roles, game, guild_id, status,
                 activities, client_status, bot_obj):
        self.user = User(**user)
        #self.roles = bot_obj.find_list("roles", roles, f"/guilds/{guild_id}/roles/"bot_obj = bot_obj)
        self.status = status
        self.text = activities
        
