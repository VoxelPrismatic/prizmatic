import re
import zlib
import json
import typing
import asyncio
import aiohttp
from . import Url
from .. import ver
from .Http import Http
from .Listener import Listener
from pprint import pprint as prinf
from .PrizmCls import PrizmList, PrizmDict

__all__ = [
    "get_json",
    "Bot"
]

class Bot:
    """
    {{cls}} bot = Bot(prefix, custom_prefix, token, *, thresh, keepalive)

    {{desc}} Your Bot!

    {{param}} prefix [str]
        The bot prefix, default is ";]". This is the fallback for when
        custom_prefix fails.

    {{param}} custom_prefix [dict, str, function]
        This is the main prefix. If a dict, then the keys are the guild
        ids, and the values are their prefixes. If a str, then the prefix
        applies to all guilds. If a function, then it must return a prefix. The
        parameters for the function will be an Info object.

    {{param}} token [str]
        This is the token from your Discord Application.

    {{param}} thresh [int]
        Timeout threshold. Don't change this if you aren't sure what it does.

    {{param}} keepalive [bool]
        Whether to reconnect to Discord upon a disconnect. Default is True

    {{prop}} prefix [str]
        Provided prefix

    {{prop}} custom_prefix [dict, str, function]
        Provided custom prefix

    {{prop}} commands [dict]
        Not really a dict, but basically the same.
        Holds all command data

    {{prop}} shards [dict]
        Not really a dict, but bascially the same.
        Holds the shards

    {{prop}} token [str]
        Provided token. Stripped content because you might want to read the
        token from another file.

    {{prop}} client [asyncio.ClientSession]
        HTTP Client for interacting with Discord

    {{prop}} thresh [int]
        Provided threshold, default is 150

    {{prop}} heartbeat [int]
        Heartbeat interval in milliseconds

    {{prop}} uri [str]
        The gateway url

    {{prop}} http_uri [str]
        The HTTP API url

    {{prop}} ack [int]
        Number of messages recieved from the gateway

    {{prop}} connected [bool]
        Whether or not the client is connected

    {{prop}} keepalive [bool]
        Provided keepalive

    {{prop}} __version__ [str]
        Version of the module

    {{prop}} listener [discord.Listener]
        Listeners, for um idk listening to events

    {{prop}} voices [dict]
        Not really a dict, but basically the same.
        Holds all VoiceClient objects and IDs

    {{prop}} http [~/Http]
        The HTTP client/interface

    {{prop}} skip_next [bool]
        Whether or not to skip the next listener, useful for creating objects
        inside this wrapper to prevent duplicate objects
    """
    def __init__(self, prefix: str = ";]", custom_prefix = ";]",
                 token: str = "", *, thresh: int = 150,
                 keepalive: bool = True):
        self.prefix = prefix
        self.custom_prefix = custom_prefix
        self.commands = PrizmDict()
        self.shards = PrizmDict()
        self.token = token.strip()
        self.client = aiohttp.ClientSession()
        self.thresh = thresh
        self.heartbeat = 45000
        self.uri = Url.gateway
        self.http_uri = Url.api
        self.http = Http(self.client, self)
        self.ack = 0
        self.connected = False
        self.keepalive = keepalive
        self.__version__ = ver.__ver__
        self.listeners = Listener(self)
        self.voices = PrizmDict()
        self.ws = None
        self.skip_next = False

    def run(self, token = "") -> None:
        """
        {{fn}} instance.run(token)

        {{desc}} Starts the bot

        {{param}} token [str]
            The token
            {{norm}} The token provided upon initialization
        """
        token = token or self.token
        if not token:
            print("No token")
            raise ValueError("No token was provided")
        self.token = token
        task = asyncio.ensure_future(self.login())

    async def send_beat(self) -> None:
        """
        {{fn}} await instance.send_beat()

        {{desc}} Sends a heartbeat to discord

        {{note}} This function is used internally, and is not meant to be used
        by hand
        """
        while self.connected:
            print(".")
            await self.ws.send_json({"op": 1, "d": self.ack})
            print(self.heartbeat / 1000)
            await asyncio.sleep(self.heartbeat / 1000)

    async def req(self, **kw):
        """
        {{fn}} await instance.req(**kw)

        {{desc}} Short for instance.http.req(**kw)

        {{param}} **kw [kwargs]
            Kwargs for http.req()

        {{rtn}} [Any] What ever was returned
        """
        return await self.http.req(**kw)

    async def _gate(self, **payload) -> dict:
        """
        {{fn}} await instance._gate(**payload)

        {{desc}} Sends a payload to the Discord Websocket

        {{note}} This function is used internally, and is not meant to be used
        by hand

        {{param}} **payload [kwargs]
            The payload

        {{rtn}} [dict] The response from the websocket
        """
        await self.ws.send_json(payload)
        m = await self.ws.receive()
        return get_json(m)

    #Shortcuts and helpers for finding stuff
    async def make(self, cl, id, url):
        """
        {{fn}} await instance.make(cl, id, url)

        {{desc}} Returns an object or creates it from a URL

        {{note}} This function is used internally, and is not meant to be used
        by hand

        {{param}} cl [str]
            Name of the group

        {{param}} id [str, int]
            ID of the object

        {{param}} url [str]
            Where to find the object

        {{rtn}} [any] The object found or made
        """
        return await self.listeners.find(cl, id, url)

    def raw(self, c, objs, *a, **kw):
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

        {{rtn}} [Any] The object found or made
        """
        return self.listeners.raw_make(c, objs, *a, **kw)

    def raw_many(self, objs, *args, **kwargs):
        """
        {{fn}} instance.raw_many(objs, *args, *kwargs)

        {{desc}} A bunch of `instance.raw()` calls

        {{note}} This function is used internally, and is not meant to be used
        by hand

        {{param}} objs [list]
            A list of args and kwargs used for calling `instance.raw()`.
            `[c, [objs], *args, {kwargs}]`, where `*args` and `{kwargs}` are
            optional and do NOT need to be included

        {{param}} *args, **kwargs [args, kwargs]
            These are global

        {{note}} This function does return everything as a tuple

        {{rtn}} [List[Any]] The objects found or made
        """
        ls = []
        for obj in objs:
            c = obj[0]
            o = obj[1]
            a = []
            kw = {}
            if len(obj) >= 3:
                a = obj[2:]
            if type(obj[-1]) == dict:
                a = a[:-1]
                kw = obj[-1]
            ls.append(self.raw(c, o, *a, *args, **kw, **kwargs))
        return ls

    def raw_edit(self, c, obj, *a, **kw):
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
        return self.listeners.raw_edit(c, obj, *a, **kw)

    async def await_make(self, c, raw_obj, **kw):
        """
        {{fn}} await instance.await_make(c, raw_obj, **kw)

        {{desc}} Similar to raw(), but is awaitable and uses Raw instead

        {{note}} This function is used internally, and is not meant to be used
        by hand

        {{param}} c [str]
            Name of the group

        {{param}} raw_obj [Raw]
            The Raw object

        {{param}} **kw [kwargs]
            Global attributes if the object needs to be created

        {{rtn}} [any] The object found or made
        """
        o = await raw_obj
        return self.bot.raw_make(c, o, **kw)

    def find(self, c, id, url = "", fmt = {}, **kw):
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
        return self.listeners.find(c, id, url, fmt, **kw)

    async def login(self):
        """
        {{fn}} await instance.login()

        {{desc}} Logs in the bot

        {{note}} Do not use this function. Use `bot.run()` instead. This is
        because you will need to use `asyncio.run(bot.login)` which is redundant
        and will prevent the bot from continuing to run properly.
        """
        print("LOGGING IN")
        data = {
            "token": self.token,
            "compress": True,
            "properties": {
                "$os": "linux",
                "$browser": "PRIZMATIC",
                "$device": "PRIZMATIC"
            },
            "large_threshold": self.thresh,
            "guild_subscriptions": True
        }
        self.http.token = self.token
        base_uri = await self.http.payload(self, data, 10, route = self.uri)
        print("here")
        self.uri = base_uri["url"] + "?v=6&encoding=json"
        async with aiohttp.ClientSession() as c:
            async with c.ws_connect(self.uri) as ws:
                self.ws = ws
                print("FINDING GATEWAY")
                await self._gate(d = data, op = 2)
                print("LOGGED IN")
                self.connected = True
                asyncio.ensure_future(self.send_beat())
                async for m in ws:
                    if self.skip_next:
                        self.skip_next = False
                        continue
                    j = get_json(m)
                    print(j)
                    if j["op"] == 10:
                        print("Got Heartbeat")
                        self.heartbeat = j["d"]["heartbeat_interval"]
                        print(self.heartbeat)
                    if j["op"] == 0:
                        await self.listeners.act(j, bot_obj = self)

    #Named aliases/shortcuts
    @property
    def all_channels(self):
        return self.listeners.channels

    @property
    def channels(self):
        return self.listeners.text_channels

    @property
    def vcs(self):
        return self.listeners.vcs

    @property
    def dms(self):
        return self.listeners.dms

    @property
    def group_dms(self):
        return self.listeners.group_dms

    @property
    def catagories(self):
        return self.listeners.catagories

    @property
    def news_channels(self):
        return self.listeners.news_channels

    @property
    def store_channels(self):
        return self.listeners.store_channels

    @property
    def texts(self):
        return self.listeners.texts

    @property
    def guilds(self):
        return self.listeners.guilds

    @property
    def emojis(self):
        return self.listeners.emojis

    @property
    def roles(self):
        return self.listeners.roles

    @property
    def players(self):
        return self.listeners.players

    @property
    def users(self):
        return self.listeners.users

    @property
    def reactions(self):
        return self.listeners.reactions

    @property
    def webhooks(self):
        return self.listeners.webhooks

    @property
    def invites(self):
        return self.listeners.invites

    @property
    def integrations(self):
        return self.listeners.integrations

    @property
    def widgets(self):
        return self.listeners.widgets

    @property
    def audits(self):
        return self.listeners.audits

    @property
    def bans(self):
        return self.listeners.bans

    @property
    def statuses(self):
        return self.listeners.statuses

    @property
    def listener(self):
        return self.listeners

def get_json(data) -> dict:
    """
    {{sepfn}} get_json(data)

    {{desc}} Returns the JSON data sent by the discord gateway

    {{param}} data [str, bytes]
        If str, then it must be raw JSON
        If bytes, then it must be ZLIB decodable and be JSON

    {{rtn}} [dict] The gateway response
    """
    if type(data) == dict:
        return data
    try:
        data = data.data
    except AttributeError:
        pass
    try:
        j = json.loads(data) #Raw JSON
    except Exception:
        try:
            j = json.loads(zlib.decompress(data)) #Compressed JSON
        except json.JSONDecodeError:
            raise TypeError("Data cannot be decoded from ZLIB or JSON")
    return j
