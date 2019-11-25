from .Color import Color, grab_color
from .Perms import Perms
from .NonExistentObj import NonExistentObj

class Role:
    """
    DESCRIPTION ---
        Represents a role
        
    PARAMS ---
        This class shouldn't be initialized by hand. Don't do that.
        
    FUNCTIONS ---
        None yet
    """
    def __init__(self, id, name, color, hoist, position, permissions, managed,
                 mentionable, guild_id = 0, bot_obj = None):
        self.id = int(id)
        self.name = name
        self.color = Color(color)
        self.hoist = hoist
        self.position = int(position)
        self.perms = Perms(permissions)
        self.managed = managed
        self.pingable = mentionable
        self.guild_id = guild_id
        self.guild = bot_obj.find("guilds", guild_id, bot_obj = bot_obj)
        self.bot_obj
        self.ping = f"<@&{self.id}>"
    
    async def edit(self, *, name = None, perms: Perms = None, color = None,
                   hoist: bool = None, pingable: bool = None, reason = None,
                   pos = None):
        ops = {}
        if hoist is not None:
            ops["hoist"] = hoist
        if pingable is not None:
            ops["mentionable"] = pingable
        if perms is not None:
            ops["permissions"] = perms.allow_int
        if color is not None:
            ops["color"] = grab_color(color)
        if name is not None:
            ops["name"] = str(name)
        if reason is not None:
            ops["r"] = reason
        if ops:
            o = await self.bot_obj.http.edit_role(self.guild_id, self.id, ops)
            self.__init__(**o)
        if pos is not None:
            o = await self.bot_obj.http.edit_roles_pos(self.guild_id, self.id, pos)
            for obj in o:
                self.bot_obj.find_existing("roles", obj["id"]).pos = obj["position"]
    
    def __dict__(self):
        return {
            "id": self.id,
            "name": self.name,
            "color": self.color,
            "permissions": self.perms,
            "position": self.position,
            "hoist": self.hoist,
            "managed": self.managed,
            "mentionable": self.pingable
        }
        
    async def delete(self, reason = None):
        await self.bot_obj.http.delete_role(self.guild_id, self.id, r = reason)
        o = NonExistentObj(f"/guilds/{self.guild_id}/roles/{self.id}", self.__class__,
                           data = {
                               "name": self.name,
                               "color": int(self.color),
                               "permissions": self.perms.allow_int,
                               "hoist": self.hoist,
                               "mentionable": self.pingable
                           }, edit = {
                               "pos": self.pos
                           })
    
