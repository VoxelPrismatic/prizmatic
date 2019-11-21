from ..ClsUtil import from_ts
from .Channel import AnyChannel
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
from . import Events
from .Voice import VoiceRegion, VoiceClient
from .Integration import Integration
from .Webhook import Webhook
from .Widget import Widget
from .GuildEmbed import GuildEmbed
from . import Semi

class Listener:
    """
    DESCRIPTION ---
        Cleans up code and provides an easy solution to listening 
        and ignoring things
    
    PARAMS ---
        This class shouldn't be initialized by hand. Don't do that.
        This class is used internally to help clean up code, don't 
        use this class in your code because it will not work without
        extensive modification in your code
    
    FUNCTIONS ---
        listener = Listener(bot)
        - Creates a new Listener object
        
        listener.get(listener_name)
        - Returns a generator of listeners without their ignored
          things
        
        await listener.act(returned_gateway_obj)
        - Calls all respective listeners with contents of returned_gateway_obj
        
        listener.find(type, id)
        - return the respective object, otherwise create it
    """
    def __init__(self, bot_obj):
        self.bot_obj = bot_obj
        self.listeners = {
            "text": PrizmList(),
            "text_edit": PrizmList(),
            "text_delete": PrizmList(),
            "call_text": PrizmList(),
            "video_text": PrizmList(),
            "embed_text": PrizmList(),
            "file_text": PrizmList(),
            "quote_text": PrizmList(),
            "boost_text": PrizmList(),
            "join_text": PrizmList(),
            "webhook_text": PrizmList(),
            "text_pinned": PrizmList(),
            "text_bulk_delete": PrizmList(),
            
            "channel_edit": PrizmList(),
            "channel_make": PrizmList(),
            "channel_delete": PrizmList(),
            
            "guild_join": PrizmList(),
            "guild_leave": PrizmList(),
            "guild_edit": PrizmList(),
            
            "player_join": PrizmList(),
            "player_edit": PrizmList(),
            "player_leave": PrizmList(),
            "player_ban": PrizmList(),
            "player_unban": PrizmList(),
            "player_typing": PrizmList(),
            "players_chunk": PrizmList(),
            
            "emoji_make": PrizmList(),
            "emoji_edit": PrizmList(),
            "emoji_delete": PrizmList(),
            
            "role_make": PrizmList(),
            "role_edit": PrizmList(),
            "role_delete": PrizmList(),
            
            "reaction_add": PrizmList(),
            "reaction_delete": PrizmList(),
            "reactions_clear": PrizmList(),
            
            "emojis_edit": PrizmList(),
            "status_update": PrizmList(),
            "user_edit": PrizmList(),
            "voice_status_update": PrizmList(),
            "voice_server_update": PrizmList(),
            "webhooks_edit": PrizmList(),
        }
        self.ignorers = {
            "text": PrizmList(),
            "text_edit": PrizmList(),
            "text_delete": PrizmList(),
            "call_text": PrizmList(),
            "video_text": PrizmList(),
            "embed_text": PrizmList(),
            "file_text": PrizmList(),
            "quote_text": PrizmList(),
            "boost_text": PrizmList(),
            "join_text": PrizmList(),
            "webhook_text": PrizmList(),
            "text_pinned": PrizmList(),
            "text_bulk_delete": PrizmList(),
            
            "channel_edit": PrizmList(),
            "channel_make": PrizmList(),
            "channel_delete": PrizmList(),
            
            "guild_join": PrizmList(),
            "guild_leave": PrizmList(),
            "guild_edit": PrizmList(),
            
            "player_join": PrizmList(),
            "player_edit": PrizmList(),
            "player_leave": PrizmList(),
            "player_ban": PrizmList(),
            "player_unban": PrizmList(),
            "player_typing": PrizmList(),
            "players_chunk": PrizmList(),
            
            "emoji_make": PrizmList(),
            "emoji_edit": PrizmList(),
            "emoji_delete": PrizmList(),
            
            "role_make": PrizmList(),
            "role_edit": PrizmList(),
            "role_delete": PrizmList(),
            
            "reaction_add": PrizmList(),
            "reaction_delete": PrizmList(),
            "reactions_clear": PrizmList(),
            
            "emojis_edit": PrizmList(),
            "status_update": PrizmList(),
            "user_edit": PrizmList(),
            "voice_status_update": PrizmList(),
            "voice_server_update": PrizmList(),
            "webhooks_edit": PrizmList(),
        }
        self.channels = PrizmDict()
        self.texts = PrizmDict()
        self.guilds = PrizmDict()
        self.emojis = PrizmDict()
        self.roles = PrizmDict()
        self.players = PrizmDict()
        self.users = PrizmDict()
        self.reactions = PrizmDict()
        self.webhooks = PrizmDict()
        self.invites = PrizmDict()
        self.widgets = PrizmDict()
        self.integrations = PrizmDict()
    
    def get(self, listener):
        for i in self.listeners[listener]:
            for j in self.ignorers[listener]:
                if i != j:
                    yield i
    
    async def act(self, j):
        d = j["d"]
        t = j["t"]
        if t == "CHANNEL_CREATE":
            o = AnyChannel(**d)
            self.channels[o.id] = o
            for l in self.get("channel_make"):
                await l(o)
        elif t == "CHANNEL_UPDATE":
            a = AnyChannel(**d)
            b = self.channels[a.id]
            self.channels[a.id] = a
            for l in self.get("channel_edit"):
                await l(b, a)
        elif t == "CHANNEL_DELETE":
            o = AnyChannel(**d)
            del self.channels[o.id]
            for l in self.get("channel_delete"):
                await l(o)
        elif t == "CHANNEL_PINS_UPDATE":
            o = self.channels[int(d["channel_id"])]
            self.channels[o.id].latest_pin_time = from_ts()
    
    async def find(self, c, id, url):
        try:
            return self.__getattribute__(c)(id)
        except KeyError:
            objs = {
                "channels": AnyChannel,
                "guilds": Guild,
                "texts": Text,
                "emojis": Emoji,
                "roles": Role,
                "players": Player,
                "users": User,
                "reactions": Reaction,
                "webhooks": Webhook,
                "integrations": Integration,
                "invites": Invite,
                "widgets": Widget
            }
            d = await self.bot_obj.http.req(u = url)
            o = objs[c](**d)
            self.__getattr__(c)[id] = o
            return o
            