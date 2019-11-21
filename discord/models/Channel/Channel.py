from datetime.datetime import fromtimestamp as from_ts
from ..Perms import Perms
from ..Guild import Guild
from ..User import User
from ..PrizmCls import PrizmList
from ..Role import Role
from ..Raw import Raw, RawObj, RawList, RawFile
from ..Overwrite import Overwrite, Overwrites
from ..Text import Text
from ..Embed import Embed
from typing import Union
from ..File import File, Files

class Channel:
    """
    DESCRIPTION ---
        Represents a text channel
        
    PARAMS ---
        This class shouldn't be initialized by hand. Don't do that.
        
    FUNCTIONS ---
        None yet
    """
    def __init__(self, *, id, guild_id, name, type, position,
                 permission_overwrites, rate_limit_per_user, nsfw, topic,
                 last_message_id, parent_id, last_pin_timestamp, bot_obj):
        self.id = id
        self.latest_message_id = int(last_message_id)
        self.latest_pin_time = from_ts(last_pin_timestamp)
        self.latest_message = Raw(Message, last_message_id, 
                                  "/channels/{cID}/messages/{id}", cID = id)
        self.name = name
        self.overwrites = Overwrites(**permission_overwrites)
        self.pos = position
        self.slowmode = rate_limit_per_user
        self.topic = topic
        self.guild_id = guild_id
        self.guild = bot_obj.listener.guilds[guild_id]
        self.catagory_id = parent_id
        self.catagory = bot_obj.listener.channels[parent_id]
        self.bot_obj = bot_obj

    def __str__(self):
        return "#"+self.name
    def __trunc__(self):
        return f"<#{self.id}>"
    def __repr__(self):
        return f"<#Channel '{self.name}'>"
    async def edit(self, **kw):
        dic = {}
        if "name" in kw:
            dic["name"] = str(kw["name"])
        if "pos" in kw:
            dic["position"] = int(kw["pos"])
        if "topic" in kw:
            dic["topic"] = str(kw["topic"])
        if "nsfw" in kw:
            if str(kw["nsfw"]).lower() in ["true", "y", "1", "yes", "ye", "t"]:
                dic["nsfw"] = True
            else:
                dic["nsfw"] = False
        if "slowmode" in kw:
            dic["rate_limit_per_user"] = int(kw["slowmode"])
        if "overwrites" in kw:
            dic["permission_overwrites"] = dict(Overwrites)
        if "catagory" in kw:
            dic["parent_id"] = str(kw["catagory"].id)
        await self.refresh()
    async def refresh(self):
        d = await self.bot_obj.http.req(m = "/", u = f"/channels/{self.id}", d = dic)
        self.__init__(**d)
    async def send(self, text, *, tts = False, embed: Embed = {}, file: Union[File, Files]):
        d = await self.bot_obj.http.req(m = "+", u = "what")