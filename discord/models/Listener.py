import typing
import asyncio
from . import Url
from . import Semi
from . import Events
from . import NonExistentObj
from .Snow import Snow
from .Role import Role
from .Emoji import Emoji
from .Color import Color
from .Embed import Embed
from .Guild import Guild
from .Invite import Invite
from .Widget import Widget
from .Status import Status
from .Audit import AuditLog
from .Webhook import Webhook
from .ClsUtil import from_ts
from .Error import LoginError
from .Error import ClassError
from .Reaction import Reaction
from .Semi import OfflineGuild
from .Channel import AnyChannel
from .Member import Player, User
from .Text import Text, Crosspost
from .GuildEmbed import GuildEmbed
from .Integration import Integration
from .PrizmCls import PrizmDict, PrizmList
from .Voice import VoiceRegion, VoiceClient
from .Perms import Perms, Overwrite, Overwrites
from .Raw import RawList, Raw, RawObj, RawObjs, RawFile, RawAny

__all__ = ["Listener"]

class Listener:
    """
    {{cls}} instance = Listener(bot_obj)

    {{desc}} Cleans up code and provides an easy solution to listening
    and ignoring things

    {{note}} This class is used internally only. Do not initialize this class
    by hand. You can access this class by using `bot.listeners`

    {{param}} bot_obj [discord.Bot]
        The bot object

    {{prop}} bot_obj [discord.Bot]
        The bot object

    {{prop}} listeners [dict]
        The active listeners

    {{prop}} ignorers [dict]
        Similar to listeners, but used for events like wanting to listen to all
        messages except for boost messages

    {{prop}} channels [dict]
    {{prop}} vcs [dict]
    {{prop}} dms [dict]
    {{prop}} group_dms [dict]
    {{prop}} categories [dict]
    {{prop}} news_channels [dict]
    {{prop}} store_channels [dict]
    {{prop}} texts [dict]
    {{prop}} guilds [dict]
    {{prop}} emojis [dict]
    {{prop}} roles [dict]
    {{prop}} players [dict]
    {{prop}} users [dict]
    {{prop}} reactions [dict]
    {{prop}} webhooks [dict]
    {{prop}} invites [dict]
    {{prop}} integrations [dict]
    {{prop}} widgets [dict]
    {{prop}} bans [dict]
    {{prop}} audits [dict]
    {{prop}} statuses [dict]
        All of these are self explanitory.
        They are all in this format: {id: instance}
        None of these are actually dicts, but they are similar enough

    {{prop}} objs [dict]
        A conversion table from catagory to actual object

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

            "ready": PrizmList(),
            "resume": PrizmList(),
            "reconnect": PrizmList(),
            "hello": PrizmList(),
            "invalid": PrizmList(),
            "error": PrizmList(),
            "disconnect": PrizmList(),
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

            "ready": PrizmList(),
            "resume": PrizmList(),
            "reconnect": PrizmList(),
            "hello": PrizmList(),
            "invalid": PrizmList(),
            "error": PrizmList(),
            "disconnect": PrizmList(),
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
        self.bans = PrizmDict()
        self.audits = PrizmDict()
        self.objs = {
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
    def channel_type(self, t):
        """
        {{fn}} instance.channel_type(t)

        {{desc}} Returns a list of channels of a given type

        {{param}} t [int]
            The channel type

        {{rtn}} [List[discord.models.Channel]] The list of channels
        """
        ls = {}
        dic = self.channels
        for channel in dic:
            if dic[channel].type == t:
                ls[channel] = dic[channel]
        return ls
    @property
    def vcs(self):
        return self.channel_type(2)

    @property
    def dms(self):
        return self.channel_type(1)

    @property
    def categories(self):
        return self.channel_type(4)

    @property
    def group_dms(self):
        return self.channel_type(3)

    @property
    def news_channels(self):
        return self.channel_type(5)

    @property
    def store_channels(self):
        return self.channel_type(6)

    def filter(self, c, **kw):
        """
        {{fn}} objects = instance.filter(c, **kw)

        {{desc}} Filters objects that have attributes matching **kw

        {{param}} c [str]
            Name of the group

        {{param}} **kw [kwargs]
            The attributes to match

        {{rtn}} [generator] The list of things
        """
        ls = self.__getattribute__(c)
        for obj in ls:
            for attr in kw:
                if obj.__getattribute__(attr) != kw["attr"]:
                    break
            else:
                yield obj

    def get(self, listener_type: typing.Union[str, list],
            ignorer_type: typing.Union[str, list] = []):
        """
        {{fn}} listeners = instance.get(listener_type, ignorer_type)

        {{desc}} Is a generator representing the listeners that actually listen
        to this event.

        {{param}} listener_type [str, list]
            The listener string. If a list, then it will yield the listeners in
            order

        {{param}} ignorer_type [str, list]
            The thing to ignore. If a list, then if the listener is ignoring any
            item in that list, it will be ignored.

        {{rtn}} [generator] The list of functions listening to the event.
        """
        listen = listener_type
        ignore = ignorer_type
        if type(ignore) == str:
            ignore = [ignore]
        if type(listen) == str:
            listen = [listen]
        for l in listen:
            for fn in self.listeners[l]:
                for i in ignore:
                    if fn in self.ignorers[i]:
                        break
                else:
                    yield fn

    async def run(self, listener_type, ignorer_type = [], *a, **kw):
        """
        {{fn}} instance.run(listener_type, ignorer_type)

        {{desc}} Handles the calling of the listeners

        {{param}} listener_type [str, list]
            Passed directly to `instance.get()`

        {{param}} ignorer_type [str, list[
            Passed directly to `instance.get()`

        {{param}} *a, **kw [args, kwargs]
            What arguments to pass on to the listener
        """
        if type(ignorer_type) not in [list, str]:
            a = [ignorer_type]
            ignorer_type = []
        for l in self.get(listener_type, ignorer_type):
            asyncio.run(l(*a, **kw))

    async def act(self, j):
        """
        {{fn}} instance.act(j)

        {{desc}} Acts upon a gateway event

        {{param}} j [dict]
            The dict from the gateway event
        """
        d = j["d"]
        t = j["t"]
        if t == "CHANNEL_CREATE":
            o = AnyChannel(**d)
            self.channels[o.id] = o
            asyncio.run(self.run("channel_make", o))
        elif t == "CHANNEL_UPDATE":
            a = AnyChannel(**d)
            b = self.channels[a.id]
            asyncio.run(self.run("channel_edit", b, a))
            b.__init__(**d)
        elif t == "CHANNEL_DELETE":
            o = AnyChannel(**d)
            if type(self.channels[o.id]) != NonExistentObj:
                self.channels[o.id].stop_existing()
            asyncio.run(self.run("channel_delete", o))
        elif t == "CHANNEL_PINS_UPDATE":
            o = self.channels[int(d["channel_id"])]
            self.channels[o.id].latest_pin_time =\
                from_ts(d["last_pin_timestamp"])
            asyncio.run(self.run("text_pinned"), o)
        elif t == "GUILD_CREATE":
            o = Guild(**d)
            self.guilds[o.id] = o
            asyncio.run(self.run("guild_make"), o)
        elif t == "GUILD_UPDATE":
            a = Guild(**d)
            b = self.guilds[a.id]
            asyncio.run(self.run("guild_edit"), b, a)
        elif t == "GUILD_DELETE":
            o = OfflineGuild(**d)
            if type(self.guilds[o.id]) != NonExistentObj:
                self.guilds[o.id].stop_existing()
            asyncio.run(self.run("guild_delete"), o)
        elif t == "GUILD_BAN_ADD":
            g = self.guilds[d["guild_id"]]
            u = User(**d["user"])


    async def make(self, c, id, url):
        """
        {{fn}} await instance.make(c, id, url)

        {{desc}} Returns an object or creates it from a URL

        {{note}} This function is used internally, and is not meant to be used
        by hand

        {{param}} c [str]
            Name of the group

        {{param}} id [str, int]
            ID of the object

        {{param}} url [str]
            Where to find the object

        {{rtn}} [any] The object found or made
        """
        try:
            return self.__getattribute__(c)(id)
        except KeyError:
            d = await self.bot_obj.http.req(u = url)
            o = self.objs[c](**d)
            self.__getattr__(c)[id] = o
            return o

    def raw_make(self, c, o, *a, **kw):
        """
        {{fn}} instance.raw(c, objs, *a, **kw)

        {{desc}} Returns an object or creates it from provided data

        {{note}} This function is used internally, and is not meant to be used
        by hand

        {{param}} c [str]
            Name of the group

        {{param}} objs [dict, list(dict)]
            The JSON object

        {{param}} *a, **kw [args, kwargs]
            Global attributes if the object needs to be created

        {{rtn}} [any] The object found or made
        """
        if type(o) not in [tuple, list]:
            o = [o]

        ls = []
        for raw in o:
            try:
                ls.append(self.__getattribute__(c)(raw["id"]))
            except KeyError:
                obj = self.objs[c](*a, **kw, **raw)
                self.__getattribute__(c)[int(raw["id"])] = obj
                ls.append(obj)
        return ls

    def raw_edit(self, c, o, *a, **kw):
        """
        {{fn}} instance.raw_edit(c, obj, *a, **kw)

        {{edit}} Edits an object with provided data

        {{note}} This function is used internally, and is not meant to be used
        by hand

        {{param}} c [str]
            Name of the group

        {{param}} obj [str, int]
            The ID of the object

        {{param}} *a, **kw [args, kwargs]
            How to edit the object

        {{rtn}} [any] The object found or made
        """
        obj = self.objs[c](*a, **o, **kw)
        try:
            tmp = self.__getattribute__(c)[int(o["id"])]
            self.__getattribute__(c)[int(o["id"])] = obj
        except KeyError:
            self.__getattribute__(c)[o["id"]] = obj
        return obj

    def find(self, c, id, url = None, fmt = {}, **kw):
        """
        {{fn}} instance.find(c, id, url, fmt, **kw)

        {{desc}} Finds an object with a given ID, and returns it. If it doesn't
        exist, then a Raw object is returned instead.

        {{note}} This function is used internally, and is not meant to be used
        by hand

        {{param}} c [str]
            Name of the group

        {{param}} id [str, int]
            ID of the object

        {{param}} url [str]
            URL of where to find the object if it doesn't exist

        {{param}} fmt [dict]
            How to format the URL, it is used in `url.format(**fmt)`

        {{param}} **kw [kwargs]
            Additional attributes for the object's creation

        {{rtn}} [any] The object found or made
        """
        fmt["id"] = id
        urls = {
            "channels": "/channels/{id}",
            "guilds": "/guilds/{id}",
        }
        try:
            return self.__getattribute__(c)(id)
        except KeyError:
            if not url and c in urls:
                url = urls[c].format(**fmt)
            elif url:
                url = url.format(**fmt)
            else:
                raise TypeError("URL not given")
            o = RawAny(self.objs[c], url, bot_obj = self.bot_obj, **kw)
            self.__getattribute__(c)[id] = o
            return o
