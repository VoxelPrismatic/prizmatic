import interface
import json
import asyncio
import aiohttp
import zlib
from pprint import pprint as prinf
from .PrizmCls import *

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
    def __init__(self, prefix = ";]", token = None, thresh = 150):
        self.prefix = prefix
        self.commands = PrizmCls([])
        self.channels = PrizmCls([])
        self.guilds = PrizmCls([])
        self.shards = PrizmCls([])
        self.emojis = PrizmCls([])
        self.members = PrizmCls([])
        self.token = token
        self.cycle = new_cycle()
        self.heart_cycle = new_cycle()
        self.client = get_client()
        self.thresh = thresh
        self.heartbeat = None
        self.uri = "https://discordapp.com/api/gateway"
        self.http_uri = "https://discordapp.com/api/v7"
        self.ack = 5
        self.connected = False
        self.keepalive = None
        self.__version__ = "1.5.2"

    async def send_beat(self):
        while self.connected:
            print(".")
            await self.ws.send_json({"op": 1, "d": self.ack})
            await asyncio.sleep(self.heartbeat/1000)

    async def __gate(self, **payload):
        await self.ws.send_json(payload)
        m = await self.ws.receive()
        return get_json(m)

    async def __http(self, m = "GET", u = "", **data):
        m = m.upper()
        if m in ["EDIT", "/"]: m = "PATCH"
        elif m in ["REMOVE", "DEL", "-"]: m = "DELETE"
        elif m in ["CREATE", "NEW", "+"]: m = "POST"
        elif m in ["FIND", "="]: m = "GET"
        payload = {
            "headers": {
                "Authorization": f"Bot {self.token}",
                "User-Agent": f"DiscordBot (https://github.com/VoxelPrismatic/prizmatic, {self.__version__})"
            },
            "data": data
        }
        payload.update(data)
        async with self.client.request(self.http_uri + u, method = m, **payload) as m:
            return get_json(m)


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
            await self.__gate(d = data, op = 2)
            print("LOGGED IN")
            self.connected = True
            async for m in ws:
                j = get_json(m)
                print("WEBSOCKET RESPONSE ]")
                prinf(j)
                #print(j["s"])
                if j["op"] == 10:
                    print("Got Heartbeat")
                    self.heartbeat = j["d"]["heartbeat_interval"]
                    asyncio.ensure_future(self.send_beat())
                self.ack = j["s"]
