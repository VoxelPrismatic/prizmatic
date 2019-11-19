import re
import json
import zlib
from .Channel import Channel, NewsChannel, StoreChannel
from .Channel import Catagory, VC, DM, GroupDM, AnyChannel
from .Text import Text, Crosspost
from .Emoji import Emoji
from .Color import Color
from .Embed import Embed
from .Perms import Perms, Overwrite, Overwrites
from .Guild import Guild
from .PrizmCls import PrizmDict, PrizmList
from .Snow import Snow
from .Audit import AuditLog
from .Member import Player, User
from .Error import ClassError
from .Invite import Invite
from .Raw import RawList, Raw, RawObj, RawObjs, RawFile

class Http:
    """
    DESCRIPTION ---
        Cleans up code by providing functions instead of so many URLs
    
    PARAMS ---
        This class shouldn't be initialized by hand. Don't do that.
        This class is used internally, and provides no use outside
        from the inside as these functions are replicated elsewhere.
        
    FUNCTIONS ---
        Replicated elsewhere in other classes, do not use them or
        you may break code.
    """
    def __init__(self, token, client, bot):
        self.token = token
        self.client = client
        self.bot = bot
        
    async def get_json(data):
        try:
            data = await data.data
        except:
            pass
        try:
            j = json.loads(data) #Raw JSON
        except:
            try:
                j = json.loads(zlib.decompress(data)) #Compressed JSON
            except:
                j = None #Some other thing that cannot be decoded
        return j
    
    async def req(self, *, m = "GET", u = "", d = {}, **data):
        m = m.upper()
        if d == {} and data != {}:
            d = data
        if m in ["EDIT", "UPDATE", "MERGE", "EDT", "/"]: m = "PATCH"
        elif m in ["REMOVE", "DEL", "DESTROY", "DUMP", "-"]: m = "DELETE"
        elif m in ["CREATE", "NEW", "ADD", "SEND", "+"]: m = "POST"
        elif m in ["OBTAIN", "FIND", "PULL", "GRAB", "="]: m = "GET"
        elif m in ["PLACE", "PUSH", ">"]: m = "PUT"
        payload = {
            "headers": {
                "Authorization": f"Bot {self.token}",
                "User-Agent": f"DiscordBot (https://github.com/VoxelPrismatic/prizmatic, {self.__version__})"
            },
            "data": d
        }
        async with self.client.request(self.http_uri + u, method = m, **payload) as m:
            return await get_json(m)
    
    async def get_audit(self, id, user = None, action = None, before = None, 
                        limit:int = 50):
        d = {"limit": limit}
        if user is None:
            pass
        elif type(user) == User or type(user) == Player:
            d["user_id"] = user.id
        elif type(user) == int:
            d["user_id"] = user
        elif re.search("^\d{20}$", str(user)):
            d["user_id"] = int(user)
        elif type(user) == Snow:
            d["user_id"] = user.id
        else:
            raise ClassError(user, int, [str, int, User, Player, Snow])
        actions = {
            "guild_edit": 1,
            "channel_make": 10, 
            "channel_edit": 11,
            "channel_delete": 12,
            "channel_overwrites_make": 13,
            "channel_overwrites_edit": 14, 
            "channel_overwrites_delete": 15,
            "player_kick": 20,
            "player_prune": 21,
            "player_ban": 22,
            "player_unban": 23,
            "player_edit": 24,
            "player_roles_edit": 25,
            "role_make": 30,
            "role_edit": 31,
            "role_delete": 32,
            "invite_make": 40,
            "invite_edit": 41,
            "invite_delete": 42,
            "webhook_make": 50,
            "webhook_edit": 51,
            "webhook_delete": 52,
            "emoji_make": 60,
            "emoji_edit": 61,
            "emoji_delete": 62,
            "text_delete": 72
        }
        if type(action) == str:
            action = action.lower().replace(" ", "_")
            if action in actions:
                d["action_type"] = actions[action]
            elif re.search("^\d{1,2}$", action):
                d["action_type"] = int(action)
            else:
                raise TypeError(f"Action '{action}' isn't valid")
        elif type(action) == int:
            d["action_type"] = action
        else:
            raise ClassError(action, int, [int, str])
        
        if before:
            d["before"] = str(Snow(before))
        j = await self.req(u = f"/guilds/{id}/audit-logs", d = d)
        return AuditLog(**j)
        
        
    async def make_guild(self, data):
        await self.req(m = "+", u = "/guilds", d = dict(data))
    async def get_guild(self, id):
        d = await self.req(u = f"/guilds/{id}")
        return Guild(**d)
    async def edit_guild(self, id, data):
        await self.req(m = "/", u = f"/guilds/{id}", d = dict(data))
    async def delete_guild(self, id):
        await self.req(m = "-", u = f"/guilds/{id}")
    
    async def get_channels(self, id):
        d = await self.req(f"/guilds/{id}/channels")
        return [AnyChannel(**kw) for kw in d]
    async def make_channel(self, id, data):
        await self.req(m = "+", u = f"/guilds/{id}/channels", d = dict(data))
    async def get_channel(self, id):
        d = await self.req(u = f"/channels/{id}")
        return AnyChannel(**d)
    async def edit_channel(self, id, data):
        await self.req(m = "/", u = f"/channels/{id}", d = dict(data))
    async def delete_channel(self, id):
        await self.req(m = "-", u = f"/channels/{id}")
    
    def get_texts(self, id, *, around = None, before = None, after = None, 
                     limit = 50):
        d = {"limit": limit}
        if around:
            d["around"] = str(Snow(around))
        if before:
            d["before"] = str(Snow(before))
        if after:
            d["after"] = str(Snow(after))
        return RawList(Text, f"/channels/{id}/messages", d, self.bot)
    async def get_text(self, cID, tID):
        j = await self.req(u = f"/channels/{cID}/messages/{tID}")
        return Text(**j)
    async def send_text(self, id, data):
        await self.req(m = "+", u = f"/channels/{id}/messages", d = dict(data))
    async def edit_text(self, cID, tID, data):
        await self.req(m = "/", u = f"/channels/{cID}/messages/{tID}", d = dict(data))
    async def delete_text(self, cID, tID):
        await self.req(m = "-", u = f"/channels/{cID}/messages/{tID}")
    async def bulk_delete_texts(self, cID, texts):
        await self.req(m = "+", u = f"/channels/{cID}/messages", d = {"messages": texts})
        
    async def reaction_add(self, cID, tID, emoji):
        await self.req(m = ">", u = f"/channels/{cID}/messages/{tID}/reactions/{emoji}/@me")
    async def reaction_delete_own(self, cID, tID, emoji):
        await self.req(m = "-", u = f"/channels/{cID}/messages/{tID}/reactions/{emoji}/@me")
    async def reaction_delete(self, cID, tID, emoji, uID):
        await self.req(m = "-", u = f"/channels/{cID}/messages/{tID}/reactions/{emoji}/{uID}")
    def get_reactions(self, cID, tID, emoji, *, limit = 25, before = None, 
                      after = None):
        d = {"limit": limit}
        if before:
            d["before"] = str(Snow(before))
        if after:
            d["after"] = str(Snow(after))
        return RawList(User, f"/channels/{cID}/messages/{tID}/reactions/{emoji}", d, self.bot)
    async def delete_all_reactions(self, cID, tID):
        await self.req(m = "-", u = f"/channels/{cID}/messages/{tID}/reactions")
    
    
    async def edit_channel_perms(self, cID, oID, *, perms: Overwrite):
        await self.req(m = ">", u = f"/channels/{cID}/permissions/{oID}", d = dict(perms))
    async def delete_channel_perms(self, cID, oID):
        await self.req(m = "-", u = f"/channels/{cID}/permissions/{oID}")
    
    async def get_invite(self, cID):
        return RawList(Invite, f"/channels/{cID}/invites", {}, self.bot)
    async def make_invite(self, cID, data):
        await self.req(m = "+", u = f"/channels/{cID}/invites", d = data)
        
    async def trigger_typing(self, cID):
        await self.req(m = "+", u = f"/channels/{cID}/typing")
        
    def get_pins(self, cID):
        return RawList(Message, f"/channels/{cID}/pins", {}, self.bot)
    async def delete_pin(self, cID, tID):
        await self.req(m = "-", u = f"/channels/{cID}/pins/{tID}")
    async def add_pin(self, cID, tID):
        await self.req(m = ">", u = f"/channels/{cID}/pins/{tID}")
    
    async def add_group_user(self, cID, uID):
        await self.req(m = ">", u = f"/channels/{cID}/recipients/{uID}")
    async def remove_group_user(self, cID, uID):
        await self.req(m = "-", u = f"/channels/{cID}/recipients/{uID}")
    
    def get_emojis(self, gID):
        return RawList(Emoji, f"/guilds/{gID}/emojis", self.bot)
    async def get_emoji(self, gID, eID):
        d = await self.req(u = f"/guilds/{gID}/emojis/{eID}")
        return Emoji(**d)
    async def make_emoji(self, gID, data):
        await self.req(m = "+", u = f"/guilds/{gID}/emojis", d = data)
    async def edit_emoji(self, gID, eID, data):
        await self.req(m = "/", u = f"/guilds/{gID}/emojis/{eID}", d = data)
    async def delete_emoji(self, gID, eID):
        await self.req(m = "-", u = f"/guilds/{gID}/emojis/{eID}")