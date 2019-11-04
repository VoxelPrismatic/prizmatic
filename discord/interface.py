import aiohttp
import asyncio

gate_codes = {
    "4000": "An unknown error occured, trying to reconnect",
    "4001": "Woops, the library sent an invalid opcode",
    "4002": "Woops, the library sent an invalid payload",
    "4003": "Woops, the library sent a payload before actually authenticating",
    "4004": "Your token is invalid, please renew it or fix it",
    "4005": "Woops, the library tried to be a bit too legit B)",
    "4007": "Woops, the library failed to reconnect, trying again",
    "4008": "Ouch, stop doing stuff so quickly because the bot is being rate limited",
    "4009": "The session timed out, reconnecting",
    "4010": "Woops, the library sent an invalid shard id",
    "4011": "Bruh, don't try handling so many guilds on a single shard"
}

gate_ops = {
    "dispatch":  0,
    "heartbeat": 1,
    "identify":  2,
    "status":    3,
    "voice":     4,
    "resume":    6,
    "reconnect": 7,
    "request":   8,
    "invalid":   9,
    "hi":       10,
    "ack":      11
}

async def payload(self, data, opcode, seq = None, event = None, route = ""):
    payload = {
        "op": opcode,
        "d": data
    }
    if seq:
        payload["s"] = seq
    if event:
        payload["t"] = event
    async with self.client.get(self.uri+route, data = payload) as r:
        if r.status != 200:
            raise Exception(r)
        try:
            j = await r.json()
        except aiohttp.client_exceptions.ContentTypeError:
            j = await r.text()
        print(j)
        return j
