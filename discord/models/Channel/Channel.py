from ..Embed import Embed
from typing import Union
from ..File import File, Files
from ..Perms import Overwrites
from ..ClsUtil import from_ts
from ..Snow import Snow
from .. import Error

__all__ = ["Channel"]

class Channel:
    """
    {{cls}} instance = Channel(*, too_many_args_to_list_here)

    {{note}} This class shouldn't be initialized by hand. Don't do that.

    {{desc}} Represents a text channel

    {{param}} id [str, discord.models.Snow, int]
        The Channel ID

    {{param}} guild_id [str, discord.models.Snow, int]

    """
    def __init__(self, *, id, guild_id, name, type, position,
                 permission_overwrites, rate_limit_per_user, nsfw, topic,
                 last_message_id, parent_id, last_pin_timestamp, bot_obj):
        self.id = id
        self.latest_message_id = int(last_message_id)
        self.latest_pin_time = from_ts(last_pin_timestamp)
        self.name = name
        self.overwrites = Overwrites(**permission_overwrites)
        self.pos = position
        self.slowmode = rate_limit_per_user
        self.topic = topic
        self.guild_id = guild_id
        self.category_id = parent_id
        self.bot_obj = bot_obj
        self.type = type

    def __str__(self):
        return "#" + self.name

    #Named Aliases
    @property
    def ping(self):
        return f"<#{self.id}>"

    @property
    def permission_overwrites(self):
        return self.overwrites

    @property
    def position(self):
        return self.pos

    @property
    def category(self):
        return self.bot_obj.listeners.channels(self.category_id)

    @property
    def guild(self):
        return self.bot_obj.listener.guilds(self.guild_id)

    @property
    def snow(self):
        return Snow(self.id)

    @property
    def made_at(self):
        return self.snow.dt

    @property
    def latest_message(self):
        return self.bot_obj.find(
            "messages",
            self.latest_message_id,
            "/channels/{cID}/messages/{id}",
            cID = self.id
        )

    def __repr__(self):
        return f"<#Channel '{self.name}'>"

    async def edit(self, *, name = None, pos = None, position = None,
                   topic = None, nsfw = None, slowmode = None,
                   overwrites = None, permission_overwrites = None,
                   category = None):
        dic = {}
        if name is not None:
            dic["name"] = str(name)
        if pos is not None or position is not None:
            dic["position"] = int(pos or position)
        if topic is not None:
            dic["topic"] = str(topic)
        if nsfw is not None:
            if str(nsfw).lower() in ["true", "y", "1", "yes", "ye", "t"]:
                dic["nsfw"] = True
            else:
                dic["nsfw"] = False
        if slowmode is not None:
            dic["rate_limit_per_user"] = int(slowmode)
        if overwrites is not None or permission_overwrites is not None:
            dic["permission_overwrites"] =\
                dict(overwrites or permission_overwrites)
        if category is not None:
            try:
                id = str(dict(category)["id"])
            except KeyError:
                if type(category) == int:
                    id = str(category)
                elif type(category) == str:
                    try:
                        id = str(Snow(category))
                    except TypeError:
                        ls = list(self.bot_obj.listeners.filter(
                            "categories",
                            name = category,
                            guild_id = int(self.guild_id)
                        ))
                        if len(ls) == 0:
                            raise Error.ObjNotFoundError(
                                "Allowed category name, id, or object",
                                "Category object or Catagory ID as int or str or Category name"
                            )
                        id = ls[0]
            dic["parent_id"] = id
        await self.refresh()

    async def refresh(self):
        d = await self.bot_obj.http.req(m = "=", u = f"/channels/{self.id}")
        self.__init__(**d)

    async def send(self, text, *, tts = False, embed: Embed = {},
                   file: Union[File, Files]):
        d = await self.bot_obj.http.req(m = "+", u = "what")
