import interface
import json
import asyncio
import aiohttp
import zlib

def new_cycle():
    cycle = asyncio.new_event_loop()
    return cycle

def get_client():
    client = aiohttp.ClientSession()
    return client

class Bot:
    def __init__(self, prefix = ";]", token = None, thresh = 150):
        self.prefix = prefix
        self.commands = []
        self.channels = []
        self.guilds = []
        self.shards = []
        self.emojis = []
        self.members = []
        self.token = token
        self.cycle = new_cycle()
        self.heart_cycle = new_cycle()
        self.client = get_client()
        self.thresh = thresh
        self.heartbeat = None
        self.uri = "https://discordapp.com/api/gateway"
        self.ack = 5
        self.connected = False
        self.keepalive = None

    async def send_beat(self):
        while self.connected:
            print(".")
            await self.ws.send_json({"op": 1, "d": self.ack})
            await asyncio.sleep(self.heartbeat/1000)

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
            await interface.ws(self, data, 2)
            print("LOGGED IN")
            self.connected = True
            async for m in ws:
                try:
                    j = json.loads(m.data)
                except:
                    d = zlib.decompress(m.data)
                    j = json.loads(d)
                print("WEBSOCKET RESPONSE ]", j)
                if j["op"] == 10:
                    print("Got Heartbeat")
                    self.heartbeat = j["d"]["heartbeat_interval"]
                    asyncio.ensure_future(self.send_beat())
                if j["op"] == 0:
                    self.ack = j["s"]


    async def send_direct(self, data, opcode, seq = None, event = None):
        await interface.ws(self, data, opcode, seq, event)
