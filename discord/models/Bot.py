import interface
import json
import asyncio
import aiohttp
import zlib
from pprint import pprint as prinf
import .Url
from .PrizmCls import PrizmList, PrizmDict, PrizmInt
from .Listener import Listener
import re

def new_cycle():
    cycle = asyncio.new_event_loop()
    return cycle

def get_client():
    client = aiohttp.ClientSession()
    return client

def get_json(data):
    try:
        data = data.data
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
        
    FUNCTIONS ---
        bot = Bot(prefix, token)
        - Creates a new Bot object
        
        @bot.listen()
        async def listener(...)
        - Make a listener
        
        @bot.on(listener_name)
        async def unnamed_listener(...)
        - Make a listener
        
        bot.listen_for(listener_function, ?listener_name)
        - Make a listener
        
        bot.stop_listening(listener_function, ?listener_name)
        - Remove a listener
        
        bot.wait(
    """
    def __init__(self, prefix = ";]", custom_prefix = ";]", token: str = None, thresh: int = 150):
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
        self.__version__ = "0.6.3"
        self.listener = Listener(self)
        self.voices = PrizmDict()
    
    def run(self, token = None):
        token = token or self.token
        if token is None:
            raise TypeError("No token was provided")
        self.token = token
        asyncio.ensure_future(self.login)
    
    async def send_beat(self):
        while self.connected:
            print(".")
            await self.ws.send_json({"op": 1, "d": self.ack})
            await asyncio.sleep(self.heartbeat/1000)

    async def _gate(self, **payload):
        await self.ws.send_json(payload)
        m = await self.ws.receive()
        return get_json(m)

    async def make(self, cl, id, url):
        return await self.listeners.find(cl, id, url)
        
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
        self.uri = (await interface.payload(self, data, 10))["url"] + "?v=6&encoding=json"
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