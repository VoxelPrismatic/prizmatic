from ..Embed import Embed
from typing import Union
from ..File import File, Files
from ..Perms import Overwrites
from ..ClsUtil import from_ts
from .. import Error

__all__ = ["Channel"]

class Channel:
    """
    DESCRIPTION ---
        Represents a text channel

    PARAMS ---
        This class shouldn't be initialized by hand. Don't do that.
    """
    def __init__(self, *, id, guild_id, name, type, position,
                 permission_overwrites, rate_limit_per_user, nsfw, topic,
                 last_message_id, parent_id, last_pin_timestamp, bot_obj):
        self.id = id
        self.latest_message_id = int(last_message_id)
        self.latest_pin_time = from_ts(last_pin_timestamp)
        self.latest_message = bot_obj.find(
            "messages",
            last_message_id,
            "/channels/{cID}/messages/{id}",
            cID = id
        )
        self.name = name
        self.overwrites = Overwrites(**permission_overwrites)
        self.pos = position
        self.slowmode = rate_limit_per_user
        self.topic = topic
        self.guild_id = guild_id
        self.guild = bot_obj.listener.guilds(guild_id)
        self.catagory_id = parent_id
        self.catagory = bot_obj.listener.channels(parent_id)
        self.bot_obj = bot_obj

    def __str__(self):
        return "#" + self.name

    @property
    def ping(self):
        return f"<#{self.id}>"

    def __repr__(self):
        return f"<#Channel '{self.name}'>"

    async def edit(self, *, name = None, pos = None, position = None,
                   nsfw = None, topic = None, slowmode = None, catagory = None,
                   overwrites = None, reason = None):
        """
        DESCRIPTION ---
            Edits the object on Discord's end

        PARAMS ---
            NOTE: All of these params are optional

            name [str]
            - Name of the channel

            pos [int]
            - Where it is located on the channel listing
            - This param has an alias under 'position', but this takes priority

            slowmode [int]
            - How many seconds of slowmode

            nsfw [bool]
            - Is this channel NSFW

            topic [str]
            - Channel topic

            catagory [Catagory]
            - The catagory of this channel

            overwrites [Overwrites]
            - The overwrites object representing the channel's overwrites

            reason [str]
            - Reason for this action
        """
        data = {}
        if name is not None:
            data["name"] = str(name)
        if pos is not None or position is not None:
            data["position"] = int(pos or position)
        if topic is not None:
            data["topic"] = str(topic)
        if nsfw is not None:
            if str(topic).lower() in ["true", "y", "1", "yes", "ye", "t"]:
                data["nsfw"] = True
            else:
                data["nsfw"] = False
        if slowmode is not None:
            data["rate_limit_per_user"] = int(slowmode)
        if overwrites is not None:
            data["permission_overwrites"] = dict(overwrites)
        if catagory is not None:
            data["parent_id"] = str(catagory.id)
        if data == {}:
            return #Sending empty data is useless
        obj = await self.bot_obj.http.req(
            m = "/",
            u = f"/channels/{self.id}",
            d = data,
            r = reason
        )
        self.__init__(**obj, bot_obj = self.bot_obj)

    async def refresh(self):
        """
        DESCRIPTION ---
            Refreshes this object if you think it is out of date

        RETURNS ---
            The updated channel
        """
        obj = await self.bot_obj.http.req(m = "=", u = f"/channels/{self.id}")
        self.__init__(**obj, bot_obj = self.bot_obj)
        return self

    async def send(self, text, *, tts = False, embed: Embed = {}, files = None):
        """
        DESCRIPTION ---
            Sends a message

        PARAMS ---
            text [str]
            - The message content

            NOTE: All of the following params are optional

            tts [bool]
            - Enable TTS, False by default

            embed [Embed]
            - The embed object

            files [File, Files]
            - Not implemented yet, don't use it
        """
        data = {"content": text, "tts": tts, "embed": embed}
        if files is not None:
            raise NotImplementedError("Files haven't been added yet")
        obj = await self.bot_obj.http.req(
            m = "+",
            u = f"/channels/{self.id}/messages",
            d = data
        )
        return self.bot_obj.raw("messages", **obj, bot_obj = self.bot_obj)
