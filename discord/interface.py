"""
This file just provides codes and things as a reference
"""

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
    0: "dispatch",
    1: "heartbeat",
    2: "identify",
    3: "status",
    4: "voice",
    #5 doesn't exist
    6: "resume",
    7: "reconnect",
    8: "request",
    9: "invalid",
    10: "hi",
    11: "ack"
}