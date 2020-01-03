from ..ClsUtil import from_ts
from ..Perms import Perms
from ..Member import User
from ..PrizmCls import PrizmList
from ..Role import Role
from ..Raw import Raw, RawObj, RawList, RawFile
from ..Perms import Overwrite, Overwrites

__all__ = ["VC"]

class VC:
    """
    {{cls}} instance = VC(*, too_many_args_to_list_here)

    {{desc}} Represents a voice channel. Nobody actually says "voice channel" in
    chat so the name "VC" was chosen instead.

    {{noinit}}

    {{param}} id [str, ~/Snow, int]
        The ID of the VC

    {{param}} name [str]
        Name of the VC

    {{param}} permission_overwrites [List[dict]]
        A list of overwrites

    {{param}} position [int]
        The position of the channel

    {{param}} type [int]
        Type of the channel, this should always be `2`

    {{param}} user_limit [int]
        The limit of users

    {{param}} guild_id [str, ~/Snow, int]
        The ID of the guild

    {{param}} bot_obj [~/Bot]
        The bot object

    {{prop}} id [int]
        ID of the channel

    {{prop}} name [str]
        Name of the channel

    {{prop}} overwrites [~/Perms.Overwrites]
        A list of overwrites
        {{alias}} permission_overwrites

    {{prop}} pos [int]
        The position of the channel
        {{alias}} position

    {{prop}} type [int]
        The type of channel, this should always be `2` unless you change it

    {{prop}} limit [int]
        Limit of users

    {{prop}} guild_id [int]
        ID of the guild

    {{prop}} guild [~/Guild]
        The guild itself

    {{prop}} bot_obj [~/Bot]
        The bot object
    """
    def __init__(self, *, id, name, permission_overwrites, position, type,
                 user_limit, guild_id, bot_obj = None, **kw):
        print(kw)
        exit()
        self.id = int(id)
        self.name = name
        self.overwrites = Overwrites(permission_overwrites)
        self.pos = position
        self.type = type
        self.limit = user_limit
        self.guild_id = int(guild_id)
        self.bot_obj = bot_obj

    @property
    def permission_overwrites(self):
        return self.overwrites

    @property
    def position(self):
        return self.pos

    @property
    def guild(self):
        return self.bot_obj.guilds(self.guild_id)

    async def refresh(self):
        """
        {{fn}} await instance.refresh()

        {{desc}} Refreshes the channel if you think it is out of date

        {{rtn}} [~.VC] The edited instance
        """
        d = await self.bot_obj.http.get_channel(self.id)
        self.__init__(**d, bot_obj = self.bot_obj, guild_id = self.guild_id)

    async def rename(self, name: str = None):
        """
        {{fn}} await instance.rename(name)

        {{desc}} Short for `await instance.edit(name = name)`

        {{param}} name [str]
            The new name for the channel

        {{rtn}} [~.VC] The edited instance
        """
        return await self.edit(name = name)

    async def move(self, pos: int = None):
        """
        {{fn}} await instance.move(pos)

        {{desc}} Short for `await instance.edit(pos = pos)`

        {{param}} pos [int]
            The new position for the channel

        {{rtn}} [~.VC] The edited instance
        """
        return await self.edit(pos = pos)

    async def move_under(self, category = None):
        """
        {{fn}} await instance.move_under(category)

        {{desc}} Short for `await instance.edit(category = category)`

        {{param}} category [str, int, ~.Category]
            The new channel category, set to `False` to remove the category

        {{rtn}} [~.VC] The edited instance
        """
        return await self.edit(category = category)

    async def edit(self, *, name = None, pos: int = None, position: int = None,
                   bitrate: int = None, limit: int = None, overwrites = None,
                   permission_overwrites = None, category = None):
        """
        {{fn}} await instance.edit(*, too_many_args_to_list_here)

        {{desc}} Edits the channel

        {{note}} All of these parameters are optional

        {{param}} name [str]
            The new name of the channel

        {{param}} pos [int]
            The new position of the channel
            {{alias}} position

        {{param}} bitrate [int]
            The new bitrate

        {{param}} limit [int]
            The user limit

        {{param}} overwrites [~/Perms.Overwrites, List[~/Perms.Overwrite], dict]
            The new overwrites
            {{alias}} permission_overwrites

        {{param}} category [int, str, ~.Category]
            The new channel category, change to `False` to remove the category

        {{rtn}} [~.VC] The edited instance

        {{err}} [TypeError] If the category or overwrites is invalid
        """
        dic = {}
        if name is not None and name != self.name:
            dic["name"] = str(name)
        if pos is not None or position is not None:
            if (pos or position) != self.pos:
                dic["position"] = int(pos or position)
        if bitrate is not None and bitrate != self.bitrate:
            dic["bitrate"] = bitrate
        if limit is not None and limit != self.limit:
            dic["user_limit"] = limit
        if overwrites is not None or permission_overwrites is not None:
            if (overwrites or permission_overwrites) != self.overwrites:
                ovw = overwrites or permission_overwrites
                ls = []
                if type(ovw) == list:
                    ls = ovw
                elif type(ovw) == Overwrite:
                    ls = [dict(ovw)]
                elif type(ovw) == Overwrites:
                    ls = [dict(o) for o in ovw]
                elif type(ovw) == dict:
                    for key in ovw:
                        if type(ovw[key]) == Perms:
                            ls.append({
                                "id": str(key),
                                "allow": ovw[key].allow_int,
                                "deny": ovw[key].deny_int
                            })
                            try:
                                self.bot_obj.roles(key)
                                t = "role"
                            except KeyError:
                                try:
                                    self.bot_obj.users(key)
                                    t = "member"
                                except KeyError:
                                    t = None

                            if t is not None:
                                ls[-1]["type"] = t
                            else:
                                raise TypeError(
                                    f"ID `{key}` is not for a role or a user"
                                )
            dic["permission_overwrites"] = ls
        if category is False and self.category != None:
            dic["parent_id"] = None
        elif category is not None:
            try:
                id = self.guild.categories(category)
            except KeyError:
                try:
                    id = category.id
                except AttributeError:
                    for c in self.guild.categories:
                        if c.name == category:
                            id = c.id
                            break
                    else:
                        raise TypeError(
                            "Category `" + repr(category) + "` is not valid"
                        )
            if id != self.category_id:
                dic["parent_id"] = id
        if dic:
            obj = await self.bot_obj.req(
                m = "/", u = f"/channels/{self.id}", d = dic
            )
            self.__init__(**obj)
        return self
