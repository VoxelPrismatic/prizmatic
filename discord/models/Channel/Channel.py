import aiohttp
import io
from typing import Union
from .. import Error
from ..Snow import Snow
from ..Embed import Embed
from ..File import File, Files
from ..Error import ObjNotFoundError
from ..NonExistentObj import NonExistentObj
from ..Perms import Overwrites, Overwrite, Perms
from ..ClsUtil import from_ts, dump_json, id_from_obj, extra_kw

__all__ = ["Channel"]

class Channel:
    """
    {{cls}} instance = Channel(*, too_many_args_to_list_here)

    {{desc}} Represents a text channel

    {{noinit}}

    {{param}} id [str, ~/Snow, int]
        The Channel ID

    {{param}} guild_id [str, ~/Snow, int]
        The Guild ID

    {{param}} name [str]
        The name of the channel

    {{param}} type [int]
        The type of channel, this should always be 0

    {{param}} position [int]
        The position of the channel

    {{param}} permission_overwrites [List[dict]]
        The overwrites

    {{param}} rate_limit_per_user [int]
        The slowmode delay in seconds

    {{param}} nsfw [bool]
        Whether or not the channel is marked as NSFW

    {{param}} topic [str]
        The channel's topic

    {{param}} last_message_id [str, ~/Snow, int]
        The ID of the latest message

    {{param}} parent_id [str, ~/Snow, int]
        The ID of the channel's category

    {{param}} last_pin_timestamp [str]
        The latest pin time

    {{param}} bot_obj [~/Bot]
        The bot object

    {{prop}} id [int]
        The ID of the channel

    {{prop}} name [str]
        Name of the channel

    {{prop}} pos [int]
        Position of the channel

    {{prop}} slowmode [int]
        Slowmode duration in seconds

    {{prop}} topic [str]
        The channel topic

    {{prop}} guild_id [int]
        The guild ID

    {{prop}} guild [~/Guild]
        The guild

    {{prop}} category_id [int]
        The category ID

    {{prop}} category [~.Category, None]
        The category, or None if there isn't one

    {{prop}} bot_obj [~/Bot]
        The bot object

    {{prop}} ping [str]
        Allows you to ping the channel

    {{prop}} latest_text_id [int]
        ID of the most recent text

    {{prop}} latest_text [~/Text.Text, None]
        The latest text or None if there isn't one

    {{prop}} overwrites [~/Perms.Overwrites]
        The permission overwrites of the channel
        {{alias}} permission_overwrites

    {{prop}} latest_pin_time [datetime.datetime]
        The time of the most recent pinned text

    {{prop}} type [int]
        This should always be 0 unless you change it

    {{}}
    """
    def __init__(self, *, id, guild_id, name, type, position, topic,
                 permission_overwrites, rate_limit_per_user, nsfw = False,
                 last_message_id = 0, parent_id = 0, last_pin_timestamp = None,
                 bot_obj = None, **kw):
        extra_kw(kw, "Channel")
        self.id = int(id)
        self.latest_text_id = int(last_message_id)
        self.latest_pin_time = from_ts(last_pin_timestamp)
        self.name = name
        self.overwrites = Overwrites(permission_overwrites)
        self.pos = position
        self.slowmode = rate_limit_per_user
        self.topic = topic
        self.guild_id = int(guild_id)
        self.category_id = int(parent_id)
        self.bot_obj = bot_obj
        self.type = type

    def __str__(self):
        """
        {{bltin}} instance.__str__()
        {{usage}} str(instance)

        {{desc}} Returns the channel name with a '#' in front

        {{rtn}} [str]
        """
        return "#" + self.name

    #Named Aliases
    @property
    def ping(self):
        return "<#" + str(self.id) + ">"

    @property
    def latest_text(self):
        if self.latest_text_id:
            return self.bot_obj.texts(self.latest_text_id)
        return None

    @property
    def permission_overwrites(self):
        return self.overwrites

    @property
    def position(self):
        return self.pos

    @property
    def category(self):
        if self.category_id:
            return self.bot_obj.all_channels(self.category_id)
        return None

    @property
    def guild(self):
        return self.bot_obj.guilds(self.guild_id)

    @property
    def made_at(self):
        return self.snow.dt

    @property
    def snow(self):
        return Snow(self.id)

    @property
    def texts(self):
        for text in self.bot_obj.texts:
            if text.channel_id == self.id:
                yield text

    def __repr__(self):
        """
        {{bltin}} instance.__repr__()
        {{usage}} repr(instance)

        {{pydesc}} __repr__

        {{rtn}} [str]
        """
        return f"<#Channel '{self.name}'>"

    async def edit(self, *, name = None, pos: int = None, position: int = None,
                   topic: str = None, nsfw: bool = None, slowmode: int = None,
                   overwrites = None, permission_overwrites = None,
                   category = None):
        """
        {{fn}} await instance.edit(*, too_many_args_to_list_here)

        {{desc}} Edits the channel

        {{note}} All of these parameters are optional

        {{param}} name [str]
            The new name of the channel

        {{param}} pos [int]
            The new position of the channel
            {{alias}} position

        {{param}} topic [str]
            The new channel topic

        {{param}} nsfw [bool]
            Whether or not the channel is NSFW

        {{param}} slowmode [int]
            Slowmode duration in seconds

        {{param}} overwrites [~/Perms.Overwrites, List[~/Perms.Overwrite], dict]
            The new overwrites
            {{alias}} permission_overwrites

        {{param}} category [int, str, ~.Category]
            The new channel category, change to `False` to remove the category

        {{rtn}} [~.Channel] The edited instance

        {{err}} [TypeError] If the category or overwrites is invalid
        """
        dic = {}
        if name is not None and name != self.name:
            dic["name"] = str(name)
        if pos is not None or position is not None:
            if (pos or position) != self.pos:
                dic["position"] = int(pos or position)
        if topic is not None and topic != self.topic:
            dic["topic"] = str(topic)
        if nsfw is not None and nsfw != self.nsfw:
            dic["nsfw"] = nsfw
        if slowmode is not None and slowmode != self.slowmode:
            dic["rate_limit_per_user"] = int(slowmode)
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

    async def refresh(self):
        """
        {{fn}} await instance.refresh()

        {{desc}} Refreshes the channel if you think it is out of date

        {{rtn}} [~.Channel] The edited instance
        """
        d = await self.bot_obj.http.get_channel(self.id)
        self.__init__(**d, bot_obj = self.bot_obj, guild_id = self.guild_id)

    async def send(self, text: str, *, tts: bool = False, embed = {},
                   file = []):
        """
        {{fn}} await instance.send(text, *, tts, embed, file)

        {{desc}} Sends a text message to the channel

        {{param}} text [str]
            The content of the text message

        {{param}} tts [bool]
            Whether or not TTS is enabled
            {{norm}} False

        {{param}} embed [dict, ~/Embed]
            The embed object

        {{param}} file [List[~/File.File], ~/File.File, ~/File.Files, file]
            The files you would like to send

        {{rtn}} [~/Text.Text] The new text
        """
        request = {
            "content": text,
            "tts": tts,
            "embed": dict(embed)
        }
        form = None
        if file:
            form = aiohttp.FormData()
            form.add_field("payload_json", dump_json(request))
            if type(file) == File:
                d = await file.send()
                form.add_field(**d)
            elif type(file) == Files:
                for f in await file.send():
                    form.add_field(**d)

        payload = {
        }
        if form is None:
            payload["d"] = request
        else:
            payload["f"] = form

        d = await self.bot_obj.http.send_text(self.id, payload)
        return d

    async def rename(self, name: str = None):
        """
        {{fn}} await instance.rename(name)

        {{desc}} Short for `await instance.edit(name = name)`

        {{param}} name [str]
            The new name for the channel

        {{rtn}} [~.Channel] The edited instance
        """
        return await self.edit(name = name)

    async def move(self, pos: int = None):
        """
        {{fn}} await instance.move(pos)

        {{desc}} Short for `await instance.edit(pos = pos)`

        {{param}} pos [int]
            The new position for the channel

        {{rtn}} [~.Channel] The edited instance
        """
        return await self.edit(pos = pos)

    async def toggle_nsfw(self):
        """
        {{fn}} await instance.toggle_nsfw()

        {{desc}} Short for `await instance.edit(nsfw = not instance.nsfw)`

        {{rtn}} [~.Channel] The edited instance
        """
        return await self.edit(nsfw = not self.nsfw)

    async def set_nsfw(self):
        """
        {{fn}} await instance.set_nsfw()

        {{desc}} Short for `await instance.edit(nsfw = True)`

        {{rtn}} [~.Channel] The edited instance
        """
        return await self.edit(nsfw = True)

    async def set_sfw(self):
        """
        {{fn}} await instance.set_sfw()

        {{desc}} Short for `await instance.edit(nsfw = False)`

        {{rtn}} [~.Channel] The edited instance
        """
        return await self.edit(nsfw = False)

    async def retopic(self, topic: str = None):
        """
        {{fn}} await instance.retopic(topic)

        {{desc}} Short for `await instance.edit(topic = topic)`

        {{param}} topic [str]
            The new topic for the channel

        {{rtn}} [~.Channel] The edited instance
        """
        return await self.edit(topic = topic)

    async def move_under(self, category = None):
        """
        {{fn}} await instance.move_under(category)

        {{desc}} Short for `await instance.edit(category = category)`

        {{param}} category [str, int, ~.Category]
            The new channel category, set to `False` to remove the category

        {{rtn}} [~.Channel] The edited instance
        """
        return await self.edit(category = category)

    async def history(self, *, limit = 50, before = None, near = None,
                      after = None):
        """
        {{fn}} await instance.history(*, limit, before, near, after)

        {{desc}} A bunch of messages
        """
        for x in range(limit // 100 + 1):
            if limit > 100:
                lim = 100
            else:
                lim = limit
            payload = {
                "limit": lim
            }
            if before is not None:
                before = id_from_obj(before, cl = "Text")
                payload["before"] = before
            if after is not None:
                after = id_from_obj(after, cl = "Text")
                payload["after"] = after
            if near is not None:
                near = id_from_obj(near, cl = "Text")
                payload["around"] = near
            for text in await self.bot_obj.http.get_texts(**payload):
                try:
                    text = self.bot_obj.listener.texts(text.id)
                except KeyError:
                    self.bot_obj.listener.texts[text.id] = text
                #Allows editing of existing objects rather than wasting RAM
                before = text.id
                yield text
            limit -= 100

    def get_text(self, id: int):
        """
        {{fn}} instance.get_text(id)

        {{desc}} Gets a text given an ID

        {{param}} id [int]
            ID of the text

        {{rtn}} [~/Text.Text, None] The text, or None if it wasn't found
        """
        for text in self.texts:
            if text.id == id:
                return text
        return None

    async def find_text(self, id: int):
        """
        {{fn}} await instance.find_text(id)

        {{desc}} Gets a text given an ID. This is basically the same as
        `instance.get_text(id)` except for this function can also make the text
        object if it wasn't found

        {{param}} id [int]
            ID of the text

        {{rtn}} [~/Text.Text, None] The text, or None if it wasn't found
        """
        t = self.get_text(id)
        if t is not None:
            return t
        t = await self.bot_obj.make(
            "texts", id, f"/channels/{self.id}/messages/{id}"
        )
        return t

    async def delete(self):
        """
        {{fn}} await instance.delete()

        {{desc}} Deletes the object and all corrosponding messages, overwrites,
        etc

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
                "type": 0,
                "topic": self.topic,
                "rate_limit_per_user": self.slowmode,
                "position": self.position,
                "permission_overwrites": [dict(ovw) for ovw in self.overwrites],
                "parent_id": self.category_id,
                "nsfw": self.nsfw
            },
            {},
            bot_obj = self.bot_obj,
            guild_id = self.guild_id
        )
        await self.bot_obj.http.delete_channel(id)
        return self
