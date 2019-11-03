import interface
import json
import asyncio

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
        self.cycle = interface.get_cycle()
        self.client = interface.get_client()
        self.thresh = thresh
        self.heartbeat = None
        self.uri = "https://discordapp.com/api/gateway"

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
            await interface.ws(self, data, 10)
            print("LOGGED IN")
            async for m in ws:
                j = json.loads(m.data)
                if j["op"] == 10:
                    self.heartbeat = j["d"]["heartbeat_interval"]
                    await self.send_beat(j["s"])
                print(j)

    async def send_beat(self, seq):
        while True:
            print(self.ws)
            await interface.ws(self, seq, 10)
            await asyncio.sleep(self.heartbeat / 1000)

    async def send_message(self, message, channel, guild):
        pass
