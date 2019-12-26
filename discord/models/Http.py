import re
import json
import zlib
from .Channel import AnyChannel
from .Text import Text, Crosspost
from .Emoji import Emoji
from .Color import Color
from .Embed import Embed
from .Perms import Perms, Overwrite, Overwrites
from .Guild import Guild
from .Error import LoginError
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
from .Role import Role
from .Widget import Widget
from .GuildEmbed import GuildEmbed
from . import Semi
from . import Url
import aiohttp

__all__ = ["Http"]

class Http:
    """
    {{cls}} instance = Http(client, bot)

    {{desc}} Cleans up code by providing functions instead of so many URLs.

    {{note}} This class is used internally to interact with discord. Do not
    initialize this class.

    {{param}} client [aiohttp.ClientSession]
        The client

    {{param}} bot [discord.models.Bot]
        The bot

    {{prop}} client [aiohttp.ClientSession]
        The client

    {{prop}} bot [discord.models.Bot]
        The bot

    {{prop}} token [str]
        Obtained from the bot object

    {{note}} This class contains many functions to interact with discord easily.
    Only the main function will be documented and other smaller functions will
    be documented.
    """
    def __init__(self, client, bot):
        self.client = client
        self.bot = bot
        self.token = bot.token
        self.limits = {}

    async def get_json(self, data):

        try:
            data = await data.data
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
    def dump_json(self, dic):
        return json.dumps(dic, separators = [",", ":"], ensure_ascii = True)
    #async def ratelimit_timeout(timeout, kwargs)

    async def req(self, *, m = "GET", u = "", t = "j", r = None, f = None,
                  d = {}, **data):
        """
        {{fn}} await instance.req(*, m, u, t, r, fd, **data)

        {{note}} This function is asyncronous, so it must be awaited

        {{warn}} Using this function is dangerous. Do not use it unless you know
        what you're doing in relation to the API

        {{desc}} Sends a payload to the API
        """
        m = m.upper()
        if d == {} and data != {}:
            d = data
        if "r" in d:
            r = d["r"]
            del d["r"]
        meth = {
            "PATCH": ["EDIT", "UPDATE", "MERGE", "/"],
            "DELETE": ["REMOVE", "DEL", "DESTROY", "-"],
            "POST": ["CREATE", "NEW", "ADD", "+"],
            "GET": ["PULL", "GRAB", "FIND", "="],
            "PUT": ["PLACE", "PUSH", "APPEND", ">"],
            "CONNECT": ["ESTABLISH", "TUNNEL", "TARGET", "&"],
            "OPTIONS": ["DATA", "OTHER", "OPTS", "?"],
            "HEAD": ["TOP", "HEADER", "HEADERS", "^"],
            "TRACE": ["TRACK", "PATH", "FOLLOW", "$"]
        }
        for M in meth:
            if m in meth[M]:
                m = M
                break
        else:
            raise TypeError("Invalid request type '" + m + "'")
        url = "https://github.com/VoxelPrismatic/prizmatic"
        payload = {
            "headers": {
                "Authorization": f"Bot {self.token}",
                "User-Agent":
                    f"DiscordBot ({url}, {self.bot.__version__})",
            },
        }
        if f is not None:
            if d or data:
                f.add_field("payload_json", self.dump_json(d or data))
            payload["data"] = f
        else:
            payload["data"] = d or data
        if not u.startswith("https://"):
            u = self.http_uri + u
        async with self.client.request(u, method = m, reason = r, **payload)\
                as w:
            if t.lower() in ["json", "j"]:
                return await self.get_json(w)
            if t.lower() in ["text", "t"]:
                return await w.text(encoding = "utf-8")
            if t.lower() in ["byte", "b"]:
                return await w.read()
    async def payload(self, data, opcode, seq = None, event = None, route = ""):
        payload = {
            "op": opcode,
            "d": data
        }
        if seq:
            payload["s"] = seq
        if event:
            payload["t"] = event
        async with self.client.get(self.bot.uri + route, data = payload) as r:
            if r.status != 200:
                raise LoginError(r.status, await r.json())
            try:
                j = await r.json()
            except aiohttp.client_exceptions.ContentTypeError:
                j = await r.text()
            print(j)
            return j

    async def get_audit(self, id, user = None, action = None, before = None,
                        limit: int = 50, **kw):
        d = {"limit": limit}
        if user is None:
            pass
        elif type(user) == User or type(user) == Player:
            d["user_id"] = user.id
        elif type(user) == int:
            d["user_id"] = user
        elif re.search(r"^\d{20}$", str(user)):
            d["user_id"] = int(user)
        elif type(user) == Snow:
            d["user_id"] = user.id
        else:
            raise ClassError(user, int, [str, int, User, Player, Snow])
        actions = {
            "guild_edit": 1,
            "channel_make": 10,
            "channel_edit": 11,
            "channel_delete": 12,
            "channel_overwrites_make": 13,
            "channel_overwrites_edit": 14,
            "channel_overwrites_delete": 15,
            "player_kick": 20,
            "player_prune": 21,
            "player_ban": 22,
            "player_unban": 23,
            "player_edit": 24,
            "player_roles_edit": 25,
            "role_make": 30,
            "role_edit": 31,
            "role_delete": 32,
            "invite_make": 40,
            "invite_edit": 41,
            "invite_delete": 42,
            "webhook_make": 50,
            "webhook_edit": 51,
            "webhook_delete": 52,
            "emoji_make": 60,
            "emoji_edit": 61,
            "emoji_delete": 62,
            "text_delete": 72
        }
        if type(action) == str:
            action = action.lower().replace(" ", "_")
            if action in actions:
                d["action_type"] = actions[action]
            elif re.search(r"^\d{1,2}$", action):
                d["action_type"] = int(action)
            else:
                raise TypeError(f"Action '{action}' isn't valid")
        elif type(action) == int:
            d["action_type"] = action
        else:
            raise ClassError(action, int, [int, str])

        if before:
            d["before"] = str(Snow(before))
        j = await self.req(u = f"/guilds/{id}/audit-logs", d = d)
        return AuditLog(**j, **kw)


    #Guilds
    async def make_guild(self, data, **kw):
        d = await self.req(
            m = "+",
            u = "/guilds",
            d = dict(data)
        )
        return self.bot.raw_make("guilds", d, **kw)
    async def get_guild(self, id, **kw):
        d = await self.req(
            u = f"/guilds/{id}"
        )
        return self.bot.raw_make("guilds", d, **kw)
    async def edit_guild(self, id, data, **kw):
        d = await self.req(
            m = "/",
            u = f"/guilds/{id}",
            d = dict(data),
        )
        return self.bot.raw_edit("guilds", d, **kw)
    async def delete_guild(self, id, **kw):
        return await self.req(
            m = "-",
            u = f"/guilds/{id}",
            **kw
        )

    #Channels
    def get_channels(self, id, **kw):
        d = self.req(
            u = f"/guilds/{id}/channels"
        )
        return self.bot.await_make("channels", d, **kw)
    async def make_channel(self, id, data, **kw):
        d = await self.req(
            m = "+",
            u = f"/guilds/{id}/channels",
            d = dict(data)
        )
        return self.bot.raw_make("channels", d, **kw)
    async def get_channel(self, id, **kw):
        d = await self.req(
            u = f"/channels/{id}",
            **kw
        )
        return self.bot.raw_make("channels", d)
    async def edit_channel(self, id, data, **kw):
        d = await self.req(
            m = "/",
            u = f"/channels/{id}",
            d = dict(data)
        )
        return self.bot.raw_edit("channels", d, **kw)
    async def delete_channel(self, id, **kw):
        return await self.req(
            m = "-",
            u = f"/channels/{id}",
            **kw
        )
    async def edit_channel_pos(self, gID, cID, pos, **kw):
        return await self.req(
            m = "/",
            u = f"/guilds/{gID}/channels",
            d = {"id": str(cID), "position": pos},
            **kw
        )

    #Messages
    def get_texts(self, id, *, around = None, before = None, after = None,
                  limit = 50, **kw):
        d = {"limit": limit}
        if around:
            d["around"] = str(Snow(around))
        if before:
            d["before"] = str(Snow(before))
        if after:
            d["after"] = str(Snow(after))
        o = self.req(
            u = f"/channels/{id}/messages"
        )
        return self.bot.await_make("texts", o, **kw)

    async def get_text(self, cID, tID, **kw):
        j = await self.req(
            u = f"/channels/{cID}/messages/{tID}",
            **kw
        )
        return Text(**j)
    async def send_text(self, id, data, **kw):
        o = await self.req(
            m = "+",
            u = f"/channels/{id}/messages",
            d = dict(data)
        )
        return self.bot.raw_make("texts", o, **kw)
    async def edit_text(self, cID, tID, data, **kw):
        obj = await self.req(
            m = "/",
            u = f"/channels/{cID}/messages/{tID}",
            d = dict(data),
        )
        return self.bot.raw_edit("texts", obj, **kw)
    async def delete_text(self, cID, tID, **kw):
        return await self.req(
            m = "-",
            u = f"/channels/{cID}/messages/{tID}",
            **kw
        )
    async def bulk_delete_texts(self, cID, texts, **kw):
        return await self.req(
            m = "+",
            u = f"/channels/{cID}/messages",
            d = {"messages": texts},
            **kw
        )

    #Reactions
    async def reaction_add(self, cID, tID, emoji, **kw):
        obj = await self.req(
            m = ">",
            u = f"/channels/{cID}/messages/{tID}/reactions/{emoji}/@me"
        )
        return self.bot.raw_make("reactions", obj, **kw)
    async def reaction_delete_own(self, cID, tID, emoji, **kw):
        return await self.req(
            m = "-",
            u = f"/channels/{cID}/messages/{tID}/reactions/{emoji}/@me",
            **kw
        )
    async def reaction_delete(self, cID, tID, emoji, uID, **kw):
        return await self.req(
            m = "-",
            u = f"/channels/{cID}/messages/{tID}/reactions/{emoji}/{uID}",
            **kw
        )
    async def get_reactions(self, cID, tID, emoji, *, limit = 25, before = None,
                            after = None, **kw):
        d = {"limit": limit}
        if before:
            d["before"] = str(Snow(before))
        if after:
            d["after"] = str(Snow(after))
        objs = await self.req(
            u = f"/channels/{cID}/messages/{tID}/reactions/{emoji}",
            d = d,
            **kw
        )
        return self.bot.raw_make("users", objs, bot_obj = self.bot)
    async def delete_all_reactions(self, cID, tID, **kw):
        return await self.req(
            m = "-",
            u = f"/channels/{cID}/messages/{tID}/reactions",
            **kw
        )

    #Perms
    async def edit_channel_perms(self, cID, oID, *, perms: Overwrite, **kw):
        return await self.req(
            m = ">",
            u = f"/channels/{cID}/permissions/{oID}",
            d = dict(perms),
            **kw
        )
    async def delete_channel_perms(self, cID, oID, **kw):
        return await self.req(
            m = "-",
            u = f"/channels/{cID}/permissions/{oID}",
            **kw
        )

    #Invites
    def get_channel_invites(self, cID, **kw):
        ls = self.req(
            u = f"/channels/{cID}/invites"
        )
        return self.bot.await_make("invites", ls, **kw)
    async def make_invite(self, cID, data, **kw):
        obj = await self.req(
            m = "+",
            u = f"/channels/{cID}/invites",
            d = data
        )
        return self.bot.raw_make("invites", obj, **kw)
    async def get_invites(self, gID, **kw):
        ls = await self.req(
            u = f"/guilds/{gID}/invites"
        )
        return self.bot.raw_make("invites", ls, **kw)

    async def get_integrations(self, gID, **kw):
        ls = await self.req(
            u = f"/guilds/{gID}/integrations"
        )
        return self.bot.raw_make("invites", ls, **kw)
    async def make_integration(self, gID, data, **kw):
        d = await self.req(
            m = "+",
            u = f"/guilds/{gID}/integrations",
            d = data
        )
        return self.bot.raw_make("integrations", d, **kw)
    async def edit_integration(self, gID, iID, data, **kw):
        d = await self.req(
            m = "/",
            u = f"/guilds/{gID}/integrations/{iID}",
            d = data
        )
        return self.bot.raw_edit("integrations", d, **kw)
    async def delete_integration(self, gID, iID, **kw):
        return await self.req(
            m = "-",
            u = f"/guilds/{gID}/integrations/{iID}",
            **kw
        )
    async def sync_integration(self, gID, iID, **kw):
        return await self.req(
            u = f"/guilds/{gID}/integrations/{iID}/sync",
            **kw
        )

    async def get_guild_embed(self, gID, **kw):
        d = await self.req(
            u = f"/guilds/{gID}/embed"
        )
        return self.bot.raw_make("embeds", d, **kw)
    async def edit_guild_embed(self, gID, data, **kw):
        d = await self.req(
            m = "/",
            u = f"/guilds/{gID}/embed",
            d = data
        )
        return self.bot.raw_edit("embeds", d, **kw)

    async def get_guild_vanity(self, gID, **kw):
        d = await self.req(
            u = f"/guilds/{gID}/vanity-url",
            **kw
        )
        return Semi.SemiInvite(**d)

    async def get_guild_widget(self, gID, style = "shield", **kw):
        return await self.req(
            u = f"/guilds/{gID}/widget.png",
            d = {"style": style},
            t = "b",
            **kw
        )

    async def trigger_typing(self, cID, **kw):
        return await self.req(
            m = "+",
            u = f"/channels/{cID}/typing",
            **kw
        )


    def get_pins(self, cID, **kw):
        d = self.req(
            u = f"/channels/{cID}/pins",
        )
        return self.bot.await_make("texts", d, **kw)
    async def delete_pin(self, cID, tID, **kw):
        return await self.req(
            m = "-",
            u = f"/channels/{cID}/pins/{tID}",
            **kw
        )
    async def add_pin(self, cID, tID, **kw):
        return await self.req(
            m = ">",
            u = f"/channels/{cID}/pins/{tID}",
            **kw
        )


    async def add_group_user(self, cID, uID, **kw):
        return await self.req(
            m = ">",
            u = f"/channels/{cID}/recipients/{uID}",
            **kw
        )
    async def remove_group_user(self, cID, uID, **kw):
        return await self.req(
            m = "-",
            u = f"/channels/{cID}/recipients/{uID}",
            **kw
        )


    def get_emojis(self, gID, **kw):
        d = self.req(
            u = f"/guilds/{gID}/emojis"
        )
        return self.bot.await_make("emojis", d, **kw)
    async def get_emoji(self, gID, eID, **kw):
        d = await self.req(
            u = f"/guilds/{gID}/emojis/{eID}",
        )
        return self.bot.raw_make("emojis", d, **kw)
    async def make_emoji(self, gID, data, **kw):
        d = await self.req(
            m = "+",
            u = f"/guilds/{gID}/emojis",
            d = data
        )
        return self.bot.raw_make("emojis", d, **kw)
    async def edit_emoji(self, gID, eID, data, **kw):
        d = await self.req(
            m = "/",
            u = f"/guilds/{gID}/emojis/{eID}",
            d = data
        )
        return self.bot.raw_edit("emojis", d, **kw)
    async def delete_emoji(self, gID, eID, **kw):
        return await self.req(
            m = "-",
            u = f"/guilds/{gID}/emojis/{eID}",
            **kw
        )


    async def get_player(self, gID, pID, **kw):
        d = await self.req(u = f"/guilds/{gID}/members/{pID}")
        return self.bot.raw_make("players", d, **kw)
    def get_players(self, gID, limit = 100, after = 0, **kw):
        d = self.req(
            u = f"/guilds/{gID}/members",
            d = {"limit": limit, "after": after}
        )
        return self.bot.await_make("players", d, **kw)
    async def add_player(self, gID, pID, data, **kw):
        return await self.req(
            m = ">",
            u = f"/guilds/{gID}/members/{pID}",
            d = data,
            **kw
        )
    async def edit_player(self, gID, pID, data, **kw):
        d = await self.req(
            m = "/",
            u = f"/guilds/{gID}/members/{pID}",
            d = data
        )
        return self.bot.raw_edit("players", d, **kw)
    async def edit_self_nick(self, gID, nick, **kw):
        return await self.req(
            m = "/",
            u = f"/guilds/{gID}/members/@me/nick",
            d = {"nick": nick},
            **kw
        )
    async def add_player_role(self, gID, pID, rID, **kw):
        return await self.req(
            m = ">",
            u = f"/guilds/{gID}/members/{pID}/roles/{rID}",
            **kw
        )
    async def remove_player_role(self, gID, pID, rID, **kw):
        return await self.req(
            m = "-",
            u = f"/guilds/{gID}/members/{pID}/roles/{rID}",
            **kw
        )
    async def kick_player(self, gID, pID, **kw):
        return await self.req(
            m = "-",
            u = f"/guilds/{gID}/members/{pID}",
            **kw
        )
    def get_bans(self, gID, **kw):
        d = self.req(
            u = f"/guilds/{gID}/bans"
        )
        return self.bot.await_make("bans", d, **kw)
    async def get_ban(self, gID, pID, **kw):
        d = await self.req(
            u = f"/guilds/{gID}/bans/{pID}"
        )
        return self.bot.raw_make("bans", d, **kw)
    async def ban_player(self, gID, pID, data = {}, **kw):
        return await self.req(
            m = ">",
            u = f"/guilds/{gID}/bans/{pID}",
            d = data,
            **kw
        )
    async def unban_player(self, gID, pID, **kw):
        return await self.req(m = "-", u = f"/guilds/{gID}/bans/{pID}", **kw)


    def get_roles(self, gID, **kw):
        ls = self.req(
            u = f"/guilds/{gID}/roles"
        )
        return self.bot.await_make("roles", ls, **kw)
    async def edit_roles_pos(self, gID, rID, pos, **kw):
        ls = await self.req(
            m = "/",
            u = f"/guilds/{gID}/roles",
            d = {"id": str(rID), "position": pos},
        )
        return self.bot.raw_make("roles", ls, **kw)
    async def edit_role(self, gID, rID, data, **kw):
        ls = await self.req(
            m = "/",
            u = f"/guilds/{gID}/roles/{rID}",
            d = data
        )
        return self.bot.raw_edit("roles", ls, **kw)
    async def delete_role(self, gID, rID, **kw):
        return await self.req(
            m = "-",
            u = f"/guilds/{gID}/roles/{rID}",
            **kw
        )

    async def get_prune(self, gID, days = 7, **kw):
        return await self.req(
            u = f"/guilds/{gID}/prune",
            d = {"days": days},
            **kw
        )
    async def start_prune(self, gID, days = 7, rtn = True, **kw):
        return await self.req(
            m = "+",
            u = f"/guilds/{gID}/prune",
            d = {"days": days, "compute_prune_count": rtn},
            **kw
        )

    def get_regions(self, gID, **kw):
        return RawList(
            VoiceRegion,
            f"/guilds/{gID}/regions",
            bot_obj = self.bot,
            **kw
        )
