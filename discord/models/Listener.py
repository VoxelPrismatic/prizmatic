from .ClsUtil import from_ts
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
from .Raw import RawList, Raw, RawObj, RawObjs, RawFile, RawAny
from . import Events
from .Voice import VoiceRegion, VoiceClient
from .Integration import Integration
from .Webhook import Webhook
from .Widget import Widget
from .GuildEmbed import GuildEmbed
from . import Semi
from .Status import Status

class Listener:
    """
    DESCRIPTION ---
        Cleans up code and provides an easy solution to listening 
        and ignoring things
    
    PARAMS ---
        This class shouldn't be initialized by hand. Don't do that.
    
    FUNCTIONS ---
        listener = Listener(bot)
        - Creates a new Listener object
        
        listener.get(listener_name)
        - Returns a generator of listeners without their ignored
          things
        
        await listener.act(returned_gateway_obj)
        - Calls all respective listeners with contents of returned_gateway_obj
        
        await listener.find(type, id, url)
        - Return the respective object, otherwise create it
        - Types: "channels", "texts", "emojis", "guilds", "webhooks", 
                 "integrations", "players", "users", "widgets", "invites",
                 "roles", "reactions"
        
        listener.raw_make(type, objects, *global_args, **global_kwargs)
        - Return the list of objects from the class. If it doesn't exist,
          then make it.
        - Types are the same as above
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
        self.statuses = PrizmDict()
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
    
    async def make(self, c, id, url):
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
                "widgets": Widget,
                "statuses": Status
            }
            d = await self.bot_obj.http.req(u = url)
            o = objs[c](**d)
            self.__getattr__(c)[id] = o
            return o
    
    def raw_make(self, c, o, *a, **kw):
        if type(raw) not in [tuple, list]:
            o = [o]
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
            "widgets": Widget,
            "statuses": Status
        }
        ls = []
        for raw in o:
            try:
                ls.append(self.__getattribute__(c)(raw["id"]))
            except KeyError:
                obj = objs[c](*a, **kw, **raw)
                self.__getattribute__(c)[int(raw["id"])] = obj
                ls.append(obj)
        return ls
    
    def find(self, c, id, url = None, fmt = {}, **kw):
        fmt["id"] = id
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
        urls = {
            "channels": "/channels/{id}",
            "guilds": "/guilds/{id}",
        }
        try:
            return self.__getattribute__(c)(id)
        except:
            if not url and c in urls:
                url = urls[c].format(**fmt)
            elif url:
                url = url.format(**fmt)
            else:
                raise TypeError("URL not given")
            o = RawAny(objs[c], url, bot_obj = self.bot_obj, **kw)
            self.__getattribute__(c)[id] = o
            return o
