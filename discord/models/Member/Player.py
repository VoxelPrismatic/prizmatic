from .User import User
from .. import PrizmCls
from ..Role import Role
from ..Raw import RawObjs, Raw
from ..ClsUtil import from_ts, extra_kw, id_from_obj

__all__ = ["Player"]

class Player:
    """
    {{cls}} instance = Player(*, too_many_args_to_list_here)

    {{desc}} Represents a player [or member]

    {{noinit}}

    {{param}} deaf [bool]
        Whether or not the player has been deafened

    {{param}} hoisted_role [str, ~/Snow, int]
        Hoisted role ID

    {{param}} joined_at [str]
        An ISO 8601 timestamp indicating when the player joined the guild

    {{param}} mute [bool]
        Whether or not the player has been muted

    {{param}} nick [str]
        The player's nickname

    {{param}} premium_since [str]
        An ISO 8601 timestamp indicating when the player boosted the guild

    {{param}} roles [List[str, ~/Snow, int]]
        A list of role IDs

    {{param}} user [dict]
        The user object

    {{param}} guild_id [str, ~/Snow, int]
        The guild ID

    {{param}} status [dict]
        The player's status

    {{param}} bot_obj [~/Bot]
        The bot object

    {{prop}} id [int]
        The player ID

    {{prop}} user [~.User]
        The user object

    {{prop}} mute [bool]
        Whether or not the player has been muted

    {{prop}} deaf [bool]
        Whether or not the player has been deafened

    {{prop}} nick [str]
        The player's nickname

    {{prop}} boosted_at [datetime.datetime]
        A datetime object representing when the player booted the guild

    {{prop}} role_ids [List[int]]
        A list of role IDs that the player has

    {{prop}} roles [List[~/Role]]
        A list of roles that the player has

    {{prop}} hoisted_role_id [int]
        The hoisted role ID

    {{prop}} hoisted_role [~/Role]
        The hoisted role itself

    {{prop}} discrim [int]
        The player's discriminator
        {{alias}} discriminator

    {{prop}} joined [datetime.datetime]
        A datetime object representing when the player joined the guild

    {{prop}} guild_id [int]
        The guild ID

    {{prop}} guild [~/Guild]
        The guild object

    {{prop}} bot_obj [~/Bot]
        The bot object
    """
    def __init__(self, *, deaf: bool, hoisted_role = 0, joined_at = "",
                 mute = False, nick = "", premium_since = None, roles = [],
                 user = {}, guild_id = 0, bot_obj = None, status = None, **kw):
        extra_kw(kw, "Player")
        self.user = bot_obj.raw("users", user, bot_obj = bot_obj)[0]
        self.mute = mute
        self.deaf = deaf
        self.nick = nick
        self.boosted_at = premium_since
        self.role_ids = [int(role) for role in roles]
        self.hoisted_role_id = int(hoisted_role or 0)
        self.joined = from_ts(joined_at)
        self.guild_id = int(guild_id)
        self.bot_obj = bot_obj

    @property
    def roles(self):
        return [self.bot_obj.roles(role) for role in self.roles]

    @property
    def hoisted_role(self):
        if self.hoisted_role_id:
            return self.bot_obj.roles(self.hoisted_role_id)
        return None

    @property
    def id(self):
        return self.user.id

    @property
    def discrim(self):
        return self.user.discrim

    @property
    def descriminator(self):
        return self.discrim

    @property
    def guild(self):
        return self.bot_obj.guilds(self.guild_id)

    @property
    def ping(self):
        return "<@" + str(self.id) + ">"

    def __str__(self):
        """
        {{bltin}} instance.__str__()
        {{usage}} str(instance)

        {{desc}} Returns the username and discriminator eg `PRIZ ;]#9244`

        {{rtn}} [str]
        """
        return self.name + "#" + self.discrim

    def __repr__(self):
        """
        {{bltin}} instance.__repr__()
        {{usage}} repr(instance)

        {{pydesc}} __repr__

        {{rtn}} [str]
        """

    def __dict__(self):
        """
        {{bltin}} instance.__dict__()
        {{usage}} dict(instance)

        {{pydesc}} __dict__

        {{rtn}} [dict]
        """
        return {
            "deaf": self.deaf,
            "mute": self.mute,
            "hoisted_role": str(self.hoisted_role_id),
            "joined_at": self.joined.isoformat(),
            "nick": self.nick,
            "premium_since": self.boosted_at.isoformat(),
            "roles": [str(role) for role in self.role_ids],
            "user": dict(self.user)
        }

    async def add_roles(self, *roles):
        """
        {{fn}} await instance.add_roles(*roles)

        {{desc}} Adds roles to the user

        {{param}} *roles [~/Role, int, str, ~/Snow]
            A list of roles to add to the user
        """
        all_roles = self.role_ids
        for role in roles:
            try:
                int(role)
            except ValueError:
                role = id_from_obj(role, self.guild.roles, "Role")
            if int(role) not in all_roles:
                all_roles.append(int(role))
