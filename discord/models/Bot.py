import json
import asyncio
import aiohttp
import zlib
from .. import ver
from pprint import pprint as prinf
from . import Url
from .PrizmCls import PrizmList, PrizmDict, PrizmInt
from .Listener import Listener
import re

__all__ = [
    "new_cycle",
    "get_client",
    "get_json",
    "Bot"
]

def new_cycle():
    cycle = asyncio.new_event_loop()
    return cycle

def get_client():
    client = aiohttp.ClientSession()
    return client

def get_json(data):
    try:
        data = data.data
    except AttributeError:
        pass
    try:
        j = json.loads(data) #Raw JSON
    except json.JSONDecodeError:
        try:
            j = json.loads(zlib.decompress(data)) #Compressed JSON
        except json.JSONDecodeError:
            j = None #Some other thing that cannot be decoded
    return j

class Bot:
    """
    DESCRIPTION ---
        Your Bot!

    PARAMS ---
        prefix [str]
        - The bot prefix, default is ';]'
        - This is the default prefix for everything

        custom_prefix [str, dict, function]
        - Custom prefix, overwrites the prefix when available
        - If str, then it just overwrites the prefix all the time
        - If dict, then it must be in {server_id: prefix} format,
          and will overwrite the prefix if the server id is in that
          dict
        - If function, then it will be called. If it raises an error,
          then it will use the default prefix and raise the error
          after invoking the command

        token [str]
        - Your token
    """
    def __init__(self, prefix = ";]", custom_prefix = ";]", token: str = None,
                 thresh: int = 150):
        self.prefix = prefix
        self.custom_prefix = custom_prefix
        self.commands = PrizmDict()
        self.shards = PrizmDict()
        self.token = token.strip()
        self.cycle = new_cycle()
        self.heart_cycle = new_cycle()
        self.client = get_client()
        self.thresh = thresh
        self.heartbeat = None
        self.uri = Url.gateway
        self.http_uri = Url.api
        self.ack = 5
        self.connected = False
        self.keepalive = None
        self.__version__ = ver.__ver__
        self.listener = Listener(self)
        self.voices = PrizmDict()

    def run(self, token = None) -> None:
        """
        DESCRIPTION ---
            Starts the bot

        PARAMS ---
            ?token [str]
            - The token
            - Is set to the token provided in the intialized bot if not provided
        """
        token = token or self.token
        if token is None:
            raise ValueError("No token was provided")
        self.token = token
        asyncio.ensure_future(self.login)

    async def send_beat(self) -> None:
        """
        NOTE ---
            This class is used internally, and is not meant to be used by hand

        DESCRIPTION ---
            Sends a heartbeat to discord

        PARAMS ---
            None
        """
        while self.connected:
            print(".")
            await self.ws.send_json({"op": 1, "d": self.ack})
            await asyncio.sleep(self.heartbeat / 1000)

    async def _gate(self, **payload) -> dict:
        """
        NOTE ---
            This class is used internally, and is not meant to be used by hand

        DESCRIPTION ---
            Sends a payload to the Discord Websocket

        PARAMS ---
            **payload
            - The payload

        RETURNS ---
            The response from the websocket
        """
        await self.ws.send_json(payload)
        m = await self.ws.receive()
        return await get_json(m)

    #Shortcuts and helpers for finding stuff
    async def make(self, cl, id, url):
        """
        NOTE ---
            This class is used internally, and is not meant to be used by hand

        DESCRIPTION ---
            Returns an object or creates it from a URL

        PARAMS ---
            cl [str]
            - Name of the group

            id [str, int]
            - ID of the object

            url [str]
            - Where to find the object

        RETURNS ---
            The object found or made
        """
        return await self.listeners.find(cl, id, url)
    def raw(self, c, objs, *a, **kw):
        """
        NOTE ---
            This class is used internally, and is not meant to be used by hand

        DESCRIPTION ---
            Returns an object or creates it from provided data

        PARAMS ---
            c [str]
            - Name of the group

            objs [dict, list(dict)]
            - The JSON object

            *a, **kw
            - Global attributes if the object needs to be created

        RETURNS ---
            The object found or made
        """
        return self.listeners.raw_make(c, objs, *a, **kw)
    def raw_edit(self, c, obj, *a, **kw):
        """
        NOTE ---
            This class is used internally, and is not meant to be used by hand

        DESCRIPTION ---
            Edits an object with provided data

        PARAMS ---
            c [str]
            - Name of the group

            obj [str, int]
            - The ID of the object

            *a, **kw
            - How to edit the object

        RETURNS ---
            The object found or made
        """
        return self.listeners.raw_edit(c, obj, *a, **kw)
    async def await_make(self, c, raw_obj, **kw):
        """
        NOTE ---
            This class is used internally, and is not meant to be used by hand

        DESCRIPTION ---
            Similar to raw(), but is awaitable and

        PARAMS ---
            c [str]
            - Name of the group

            raw_obj [Raw]
            - The Raw object

            **kw
            - Global attributes if the object needs to be created

        RETURNS ---
            The object found or made
        """
        o = await raw_obj
        return self.bot.raw_make(c, o, **kw)
    def find(self, c, id, url = "", fmt = {}, **kw):
        return self.listeners.find(c, id, url, fmt, **kw)
    def find_list(self, c, ids, fmt_url = "", fmt = {}, **kw):
        ls = []
        for id in ids:
            fmt["id"] = id
            ls.append(c, id, fmt_url.format(**fmt), **kw)
        return ls
    def find_existing(self, c, ids):
        if type(ids) not in [list, tuple]:
            return self.listeners.__getattribute__(c)(ids)
        else:
            ls = []
            for id in ids:
                ls.append(self.listeners.__getattribute__(c)(id))
            return ls

    async def login(self):
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
        self.uri = (await self.http.payload(self, data, 10))["url"] + "?v=6&encoding=json"
        async with self.client.ws_connect(self.uri) as ws:
            self.ws = ws
            print("FINDING GATEWAY")
            await self._gate(d = data, op = 2)
            print("LOGGED IN")
            self.connected = True
            async for m in ws:
                j = get_json(m)
                if j["op"] == 10:
                    print("Got Heartbeat")
                    self.heartbeat = j["d"]["heartbeat_interval"]
                    asyncio.ensure_future(self.send_beat())
                if j["op"] == 0:
                    self.listener.act(j)
