from ..Role import Role
from ..Snow import Snow
from ..Member import User
from ..PrizmCls import PrizmList
from ..ClsUtil import from_ts, extra_kw
from ..NonExistentObj import NonExistentObj
from ..Perms import Perms, Overwrites, Overwrite

__all__ = ["Category"]

class Category:
    """
    {{cls}} instance = Category(*, too_many_args_to_list_here)

    {{desc}} Represents a category channel

    {{note}} This class can also be an iterable for all the sub channels. See
    #/fn "__next__"()/ *for* more info. Haha I made a pun *for* you again. Ok I
    need to stop making these.

    {{noinit}}

    {{param}} permission_overwrites [List[dict]]
        A list of permission overwrites

    {{param}} name [str]
        The name of the category

    {{param}} guild_id [int, ~/Snow, str]
        ID of the guild

    {{param}} type [int]
        Type of channel, this will always be `4` unless you change it

    {{param}} id [int, ~/Snow, str]
        The ID of the category

    {{param}} position [int]
        The position of this category

    {{param}} user_limit [int]
        Number of users, this should be for VCs, idk

    {{param}} bitrate [int]
        Bitrate for VCs

    {{param}} bot_obj [~/Bot]
        The bot object
        {{optn}}

    {{prop}} id [int]
        The ID of the category

    {{prop}} name [str]
        Name of the category

    {{prop}} category_id [int]
        The ID this category is under

    {{prop}} type [int]
        The type of this category, this should always be `4` unless you change
        it

    {{prop}} pos [int]
        The position of this category
        {{alias}} position

    {{prop}} guild_id [int]
        The ID of the guild this category belongs to

    {{prop}} guild [~/Guild]
        The guild this category belongs to

    {{prop}} overwrites [~/Perms.Overwrites]
        The overwrites object
        {{alias}} permission_overwrites

    {{prop}} sub_channels [~.AnyChannel]
        All the sub channels of this category

    {{prop}} num_channels [int]
        Number of sub channels of this category

    {{prop}} channels [~.Channel]
        All the text channels of this category

    {{prop}} vcs [~.VC]
        All the VCs of this category

    {{prop}} stores [~.StoreChannel]
        All the store channels of this category

    {{prop}} news [~.NewsChannel]
        All the news channels of this category. Yes, I know it says `news`, but
        `newss` or `newses` would be awkward so I am sticking with this

    {{prop}} limit [int]
        Number of users, this should be for VCs, idk

    {{prop}} bitrate [int]
        Bitrate for VCs

    {{prop}} snow [~/Snow]
        The Snow object

    {{prop}} made_at [datetime.datetime]
        When this channel was made

    {{prop}} bot_obj [~/Bot]
        The bot object
    """
    def __init__(self, *, permission_overwrites, name, guild_id, type, id,
                 position, user_limit, bitrate, bot_obj = None, **kw):
        extra_kw(kw, "Category")
        self.overwrites = Overwrites(permission_overwrites)
        self.name = name
        self.guild_id = int(guild_id)
        self.limit = user_limit
        self.bitrate = bitrate
        self.type = type
        self.id = int(id)
        self.bot_obj = bot_obj
        self.pos = position

    def get_channels_by_type(self, type: int):
        """
        {{fn}} instance.get_channels_by_type(type)

        {{desc}} Returns a list of channels that this category "owns" given a
        channel type

        {{param}} type [int]
            The channel type

        {{rtn}} [List[~.AnyChannel]] The list of channels
        """
        ls = []
        for channel in self.guild.channels:
            if channel.category_id == self.id and channel.type == type:
                ls.append(channel)
        return ls

    @property
    def position(self):
        return self.pos

    @property
    def guild(self):
        return self.bot_obj.guilds(self.guild_id)

    @property
    def permission_overwrites(self):
        return self.overwrites

    @property
    def sub_channels(self):
        ls = []
        for channel in self.guild.all_channels:
            if channel.category_id == self.id:
                ls.append(channel)
        return ls

    @property
    def num_channels(self):
        return len(self.sub_channels)

    @property
    def channels(self):
        return self.get_channels_by_type(0)

    @property
    def vcs(self):
        return self.get_channels_by_type(2)

    @property
    def stores(self):
        return self.get_channels_by_type(6)

    @property
    def news(self):
        return self.get_channels_by_type(5)

    @property
    def snow(self):
        return Snow(self.id)

    @property
    def made_at(self):
        return self.snow.dt

    async def make_channel(self, name: str, *, topic: str = "", overwrites = [],
                           slowmode: int = 0, nsfw: bool = False):
        """
        {{fn}} await instance.make_channel(name, *, topic, overwrites, slowmode,
        nsfw)

        {{desc}} Creates a text channel under this category

        {{param}} name [str]
            The name of the new channel

        {{param}} topic [str]
            Topic of the new channel
            {{norm}} ""

        {{param}} overwrites [List[dict, ~/Perms/Overwrite], ~/Perms/Overwrites]
            Channel overwrites
            {{norm}} []

        {{param}} slowmode [int]
            The slowmode limit in seconds
            {{norm}} 0

        {{param}} nsfw [bool]
            Whether or not this channel is NSFW
            {{norm}} False

        {{rtn}} [~.Channel] The new channel
        """
        d = {
            "name": name,
            "topic": topic,
            "type": 0,
            "parent_id": str(self.id),
            "permission_overwrites": [dict(ovw) for ovw in overwrites],
            "rate_limit_per_user": slowmode,
            "nsfw": nsfw
        }
        obj = await self.bot_obj.http.make_channel(
            self.guild_id, d, bot_obj = self.bot_obj, guild_id = self.guild
        )
        return self.bot_obj.all_channels(obj.id)

    async def make_store(self, name: str, *, topic: str = "", overwrites = [],
                         slowmode: int = 0, nsfw: bool = False):
        """
        {{fn}} await instance.make_store(name, *, topic, overwrites, ...)

        {{desc}} Creates a store channel under this category

        {{note}} Only the `name` param is required

        {{param}} name [str]
            The name of the new channel

        {{param}} topic [str]
            Topic of the new channel
            {{norm}} ""

        {{param}} overwrites [List[dict, ~/Perms/Overwrite], ~/Perms/Overwrites]
            Channel overwrites
            {{norm}} []

        {{param}} slowmode [int]
            The slowmode limit in seconds
            {{norm}} 0

        {{param}} nsfw [bool]
            Whether or not this channel is NSFW
            {{norm}} False

        {{rtn}} [~.StoreChannel] The new channel
        """
        d = {
            "name": name,
            "topic": topic,
            "type": 6,
            "parent_id": str(self.id),
            "permission_overwrites": [dict(ovw) for ovw in overwrites],
            "rate_limit_per_user": slowmode,
            "nsfw": nsfw
        }
        obj = await self.bot_obj.http.make_channel(
            self.guild_id, d, bot_obj = self.bot_obj, guild_id = self.guild
        )
        return self.bot_obj.all_channels(obj.id)

    async def make_news(self, name: str, *, topic: str = "", overwrites = [],
                        slowmode: int = 0, nsfw: bool = False):
        """
        {{fn}} await instance.make_news(name, *, topic, overwrites, ...)

        {{desc}} Creates a news channel under this category

        {{note}} Only the `name` param is required

        {{param}} name [str]
            The name of the new channel

        {{param}} topic [str]
            Topic of the new channel
            {{norm}} ""

        {{param}} overwrites [List[dict, ~/Perms/Overwrite], ~/Perms/Overwrites]
            Channel overwrites
            {{norm}} []

        {{param}} slowmode [int]
            The slowmode limit in seconds
            {{norm}} 0

        {{param}} nsfw [bool]
            Whether or not this channel is NSFW
            {{norm}} False

        {{rtn}} [~.NewsChannel] The new channel
        """
        d = {
            "name": name,
            "topic": topic,
            "type": 5,
            "parent_id": str(self.id),
            "permission_overwrites": [dict(ovw) for ovw in overwrites],
            "rate_limit_per_user": slowmode,
            "nsfw": nsfw
        }
        obj = await self.bot_obj.http.make_channel(
            self.guild_id, d, bot_obj = self.bot_obj, guild_id = self.guild
        )
        return self.bot_obj.all_channels(obj.id)

    async def make_vc(self, name: str, *, bitrate: int = 64, overwrites = [],
                      limit: int = 0):
        """
        {{fn}} await instance.make_vc(name, *, bitrate, overwrites, limit)

        {{desc}} Creates a voice channel under this category

        {{note}} Only the `name` param is required

        {{param}} name [str]
            The name of the new vc

        {{param}} bitrate [int]
            The bitrate of this vc
            {{norm}} 64

        {{param}} overwrites [List[dict, ~/Perms/Overwrite], ~/Perms/Overwrites]
            Channel overwrites

        {{param}} limit [int]
            Number of users this vc can hold
            {{norm}} 0

        {{rtn}} [~.VC] The new VC
        """
        d = {
            "name": name,
            "type": 2,
            "parent_id": str(self.id),
            "permission_overwrites": [dict(ovw) for ovw in overwrites],
            "bitrate": bitrate,
            "user_limit": limit
        }
        obj = await self.bot_obj.http.make_channel(
            self.guild_id, d, bot_obj = self.bot_obj, guild_id = self.guild
        )
        return self.bot_obj.all_channels(obj.id)

    async def edit(self, *, name = None, pos: int = None, position: int = None,
                   overwrites = None, permission_overwrites = None):
        """
        {{fn}} await instance.edit(*, too_many_args_to_list_here)

        {{desc}} Edits the object

        {{note}} All parameters are optional

        {{param}} name [str]
            Name of the channel

        {{param}} pos [int]
            Position of the channel
            {{alias}} position

        {{param}} overwrites [~/Perms.Overwrites, List[~/Perms.Overwrite], dict]
            The overwrites. If a dict, then it must be in `id: perms_instance`
            key-value pairs, otherwise, it will not work
            {{alias}} permission_overwrites

        {{rtn}} [~.Category] The edited self

        {{err}} [TypeError] If any of the `id: perms_intance` pairs has an ID
        that doesn't belong to a user or a role
        """
        data = {}
        if name is not None:
            data["name"] = name
        if pos is not None or position is not None:
            if pos is not None:
                data["position"] = pos
            else:
                data["position"] = position
                #0 or None returns None, where it should be 0
        if overwrites is not None or permission_overwrites is not None:
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
                            ls[-1]["type"] = "role"
                        except KeyError:
                            try:
                                self.bot_obj.users(key)
                                ls[-1]["type"] = "member"
                            except KeyError:
                                del ls[-1]
                                raise TypeError(
                                    f"ID `{key}` is not for a role or a user"
                                )
            data["permission_overwrites"] = ls
        if data:
            d = await self.bot_obj.http.edit_channel(self.id, data)
            self.__init__(**d, bot_obj = self.bot_obj, guild_id = self.guild_id)
        return self

    async def refresh(self):
        """
        {{fn}} await instance.refresh()

        {{desc}} Refreshes the category if you think it is out of date

        {{rtn}} [~.Category] The edited self
        """
        d = await self.bot_obj.http.get_channel(self.id)
        self.__init__(**d, bot_obj = self.bot_obj, guild_id = self.guild_id)
        return self


    def __list__(self):
        """
        {{bltin}} instance.__list__()
        {{usage}} list(instance)

        {{pydesc}} __list__ subchannels

        {{rtn}} [List[~.AnyChannel]]
        """
        return self.sub_channels

    def __iter__(self):
        """
        {{bltin}} instance.__iter__()
        {{usage}} iter(instance)

        {{pydesc}} __iter__ of subchannels

        {{rtn}} [generator]
        """
        self.___iter_index___ = -1
        return self

    def __next__(self):
        """
        {{bltin}} instance.__next__()
        {{usage}} for channel in instance: #... code

        {{pydesc}} __next__ the subchannels

        {{rtn}} [~.AnyChannel]
        """
        self.___iter_index___ += 1
        if self.___iter_index___ < len(self.sub_channels):
            return self.sub_channels[self.___iter_index___]
        raise StopIteration("No more channels in this category")

    def __dict__(self):
        """
        {{bltin}} instance.__dict__()
        {{usage}} dict(instance)

        {{pydesc}} __dict__

        {{rtn}} [dict]
        """
        return {
            "permission_overwrites": [dict(ovw) for ovw in self.overwrites],
            "name": self.name,
            "parent_id": str(self.category_id) if self.category_id else None,
            "nsfw": self.nsfw,
            "position": self.pos,
            "guild_id": str(self.guild_id),
            "type": 4,
            "id": str(self.id)
        }

    async def delete(self):
        """
        {{fn}} await instance.delete()

        {{desc}} Deletes the object

        {{rtn}} [~/NonExistentObj] The deleted object that can be undeleted
        """
        for text in self.bot_obj.texts:
            del self.bot_obj.listeners[text.id]
        id = self.id
        self = NonExistentObj(
            f"/guilds/{self.guild_id}/channels",
            self.__class__,
            self.bot_obj,
            {
                "name": self.name,
                "type": 4,
                "position": self.position,
                "permission_overwrites": [dict(ovw) for ovw in self.overwrites],
            },
            {},
            bot_obj = self.bot_obj,
            guild_id = self.guild_id
        )
        await self.bot_obj.http.delete_channel(id)
        return self

    def __repr__(self):
        """
        {{bltin}} instance.__repr__()
        {{usage}} repr(instance)

        {{pydesc}} __repr__

        {{rtn}} [str]
        """
        return f"<#Category '{self.name}' {self.id}>"
