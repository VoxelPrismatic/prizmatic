from .Color import Color, grab_color
from .Perms import Perms
from .NonExistentObj import NonExistentObj

__all__ = ["Role"]

class Role:
    """
    {{cls}} instance = Role(*, too_many_args_to_list_here)

    {{desc}} Depresents a role

    {{note}} This class shouldn't be initialized by hand. Don't do that.

    {{param}} id [str]
        The role ID

    {{param}} color [int]
        The color int, like 0x00ffff being rgb(000, 255, 255)

    {{param}} hoist [bool]
        Whether or not this role is hoisted. AKA Does it seperate the player
        list

    {{param}} position [int]
        Where it is located on the role list in the server menu from the bottom

    {{param}} permissions [int]
        The permissions integer

    {{param}} managed [bool]
        Whether or not this role is managed by an integration like twitch

    {{param}} mentionable [bool]
        Whether or not this role can be pinged

    {{param}} guild_id [str, ~/Snow]
        The guild that owns this role

    {{prop}} id [int]
        Id of the object

    {{prop}} name [str]
        Name of the object

    {{prop}} color [~/Color]
        Color of the object
        {{alias}} colour

    {{prop}} hoist [bool]
        Whether or not this role shows differently on the player board

    {{prop}} position [int]
        Position on the role list, 0 is @everyone and it counts up

    {{prop}} perms [~/Perms.Perms]
        The permissions

    {{prop}} managed [bool]
        Whether or not this role is managed by an integration, eg Patreon or
        Twitch

    {{prop}} pingable [bool]
        Whether or not you can ping the object

    {{prop}} guild_id [int]
        The Guild ID

    {{prop}} guild [~/Guild]
        The guild that owns this object

    {{prop}} bot_obj [~/Bot]
        The bot object
    """
    def __init__(self, *, id: str, name: str, color: int, hoist: bool,
                 position: int, permissions: int, managed: bool,
                 mentionable: bool, guild_id = 0, bot_obj = None):
        self.id = int(id)
        self.name = name
        self.color = Color(color)
        self.hoist = hoist
        self.position = int(position)
        self.perms = Perms(permissions)
        self.managed = managed
        self.pingable = mentionable
        self.guild_id = int(guild_id)
        self.bot_obj = bot_obj

    async def edit(self, *, name = None, perms: Perms = None, color = None,
                   hoist: bool = None, pingable: bool = None, reason = None,
                   position = None, pos: int = None):
        """
        {{fn}} await instance.edit(*, too_many_args_to_list_here)

        {{note}} This function is asyncronous, so it must be awaited

        {{desc}} Edits the object on discord's end

        {{note}} All of these params are optional

        {{param}} name [str]
            The new name of the role

        {{param}} perms [int, str, ~/Perms.Perms]
            The permissions level for the role

        {{param}} color [str, int, ~/Color]
            The color-compatible color

        {{param}} hoist [bool]
            Whether or not this role should show up seperately in the player list

        {{param}} pingable [bool]
            Whether or not this object can be pinged

        {{param}} pos [int]
            The position of this role
            {{alias}} position

        {{param}} reason [str]
            The reason for this change

        {{note}} If no params are passed, no data will actually be sent to
        discord. This is to prevent wasted data usage and time
        """
        ops = {}
        if hoist is not None:
            ops["hoist"] = hoist
        if pingable is not None:
            ops["mentionable"] = pingable
        if perms is not None:
            ops["permissions"] = int(perms)
        if color is not None:
            ops["color"] = grab_color(color)
        if name is not None:
            ops["name"] = str(name)
        if reason is not None:
            ops["r"] = reason
        if ops:
            o = await self.bot_obj.http.edit_role(self.guild_id, self.id, ops)
            self.__init__(**o)
        if pos is not None or position is not None:
            o = await self.bot_obj.http.edit_roles_pos(
                self.guild_id, self.id, pos or position
            )
            #for obj in o:
            #    self.bot_obj.find_existing("roles", obj["id"]).pos = obj["position"]

    def __dict__(self):
        """
        {{fn}} instance.__dict__()

        {{note}} This function is actually meant to be used as `dict(instance)`

        {{desc}} Returns the send-ready object

        {{rtn}} [dict] The send-ready object
        """
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

    async def delete(self, reason = None) -> NonExistentObj:
        """
        {{fn}} await instance.delete(reason)

        {{note}} This function is asyncronous, so it must be awaited

        {{desc}} Deletes the object on discord's end

        {{rtn}} [~/NonExistentObj] The deleted object
        """
        await self.bot_obj.http.delete_role(self.guild_id, self.id, r = reason)
        o = NonExistentObj(
            f"/guilds/{self.guild_id}/roles/{self.id}",
            self.__class__,
            data = {
                "name": self.name,
                "color": int(self.color),
                "permissions": self.perms.allow_int,
                "hoist": self.hoist,
                "mentionable": self.pingable
            },
            edit = {
                "pos": self.pos
            }
        )

    @property
    def ping(self):
        return f"<&@{self.id}>"

    @property
    def guild(self):
        return self.bot_obj.listeners.guilds(self.guild_id)

    @property
    def colour(self):
        return self.color

    def __int__(self):
        """
        {{bltin}} instance.__int__()
        {{usage}} int(instance)

        {{desc}} Returns the role ID

        {{rtn}} [int]
        """
        return self.id
