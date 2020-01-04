from . import Url

__all__ = ["Emoji"]

class Emoji:
    """
    {{cls}} instance = Emoji(*, too_many_args_to_list_here)

    {{desc}} Represents an emoji.

    {{noinit}}

    {{param}} id [str, ~/Snow, int]
        ID of the emoji

    {{param}} name [str]
        Name of the emoji

    {{param}} require_colons [bool]
        Whether or not this emoji requires the use of colons

    {{param}} managed [bool]
        Whether or not this emoji is managed by an integration

    {{param}} roles [List[dict]]
        The roles that this emoji is limited to, if an empty list then it is
        usable by all users

    {{param}} available [bool]
        Whether or not the client is allowed to use this emoji

    {{param}} animated [bool]
        Whether or not this emoji is animated

    {{param}} guild_id [str, ~/Snow, int]
        ID of the emoji's guild

    {{param}} bot_obj [~/Bot]
        Bot object

    {{prop}} id [int]
        ID of the emoji

    {{prop}} name [str]
        Name of the emoji

    {{prop}} colons [bool]
        Whether or not this emoji requires the use of colons

    {{prop}} managed [bool]
        Whether or not this emoji is managed by an integration

    {{prop}} roles [List[~/Role]]
        The roles that this emoji is limited to, if an empty list then it is
        usable by all users

    {{prop}} usable [bool]
        Whether or not the client is allowed to use this emoji

    {{prop}} gif [bool]
        Whether or not this emoji is animated

    {{prop}} guild_id [str]
        ID of the emoji's guild

    {{prop}} guild [~/Guild]
        The guild this emoji belongs to

    {{prop}} send [str]
        The sendable form

    {{prop}} url [str]
        Url of the emoji

    {{prop}} bot_obj [~/Bot]
        Bot object
    """
    def __init__(self, *, id, name, require_colons, managed, roles, available,
                 animated, guild_id, bot_obj = None):
        self.roles = bot_obj.raw("roles", roles)
        self.colons = require_colons
        self.name = name
        self.id = int(id)
        self.usable = available
        self.managed = managed
        self.gif = animated
        self.guild_id = int(guild_id)
        self.bot_obj = bot_obj

    def __str__(self):
        """
        {{bltin}} instance.__str__()
        {{usage}} str(instance)

        {{desc}} Returns the sendable name, <:name:id>

        {{rtn}} [str]
        """
        st = "<"
        if self.gif:
            st += "a"
        st += ":" + str(self.id) + ":" + self.name + ">"
        return st

    @property
    def send(self):
        return str(self)

    @property
    def guild(self):
        return self.bot_obj.guilds(self.id)

    @property
    def url(self):
        return Url.emoji(self.id, fmt = "gif" if self.gif else "png")

    def __repr__(self):
        """
        {{bltin}} instance.__repr__()
        {{usage}} repr(instance)

        {{pydesc}} __repr__

        {{rtn}} [str]
        """
        st = "<"
        if self.gif:
            st += "Animated "
        st += "Emoji '" + self.name + "' with ID " + str(self.id) + ">"
        return st

    def __dict__(self):
        """
        {{bltin}} instance.__dict__()
        {{usage}} dict(instance)

        {{pydesc}} __dict__

        {{rtn}} [dict]
        """
        return {
            "id": str(self.id),
            "name": self.name,
            "require_colons": self.colons,
            "animated": self.gif,
            "managed": self.managed,
            "available": self.usable,
            "roles": [dict(role) for role in self.roles]
        }

    async def refresh(self):
        """
        {{fn}} await instance.refresh()

        {{desc}} Refreshes the emoji if you think it is out of date

        {{rtn}} [~.Emoji] The edited instance
        """
        d = await self.bot_obj.http.get_channel(self.id)
        self.__init__(**d, bot_obj = self.bot_obj, guild_id = self.guild_id)
