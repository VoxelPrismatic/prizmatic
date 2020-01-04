from . import Url
from .Role import Role
from .Perms import Perms
from .Emoji import Emoji
from .Member import Player
from .Error import ClassError
from .Channel import AnyChannel
from .PrizmCls import PrizmDict
from .ClsUtil import from_ts, id_from_obj

__all__ = ["Guild"]

class Guild:
    """
    {{cls}} instance = Guild(*, too_many_args_to_list_here)

    {{desc}} Represents a Guild

    {{noinit}}

    {{note}} A "guild" is referred to as a "server" in the UI

    {{param}} id [str, ~/Snow, int]
        The guild ID

    {{param}} name [str]
        The name of the guild

    {{param}} splash [str]
        Hash of the splash image

    {{param}} owner_id [str, ~/Snow, int]
        ID of the owner

    {{param}} region [str]
        Voice region of the guild

    {{param}} features [List[str]]
        A list of features available to the guild

    {{param}} afk_channel_id [str, ~/Snow, int]
        The AFK VC ID

    {{param}} afk_timeout [int]
        The AFK timeout, in seconds

    {{param}} verification_level [int]
        The level of verification the guild requires

    {{param}} emojis [List[dict]]
        A list of dict emoji objects

    {{param}} default_message_notifications [int]
        The default message notificarion level

    {{param}} explicit_content_filter [int]
        The nsfw filter level

    {{param}} roles [List[dict]]
        A list of dict role objects

    {{param}} mfa_level [int]
        The level of Multi-factor authentication

    {{param}} application_id [str, ~/Snow, int]
        The app id of the bot that created the server, None if it wasn't made by
        a bot

    {{param}} system_channel_id [str, ~/Snow, int]
        The channel ID of welcome messages, boost messages, and more

    {{param}} system_channel_flags [int]
        Flags integer for things like boost/join messages

    {{param}} rules_channel_id [str, ~/Snow, int]
        The ID of the rules channel

    {{param}} description [str]
        Description of the server

    {{param}} preferred_locale [str]
        Default language settings

    {{param}} banner [str]
        Banner hash

    {{param}} owner [bool]
        Whether or not the client is the owner of the guild

    {{param}} permissions [int]
        Permissions integer of the clienr

    {{param}} vanity_url_code [str]
        Vanity URL, eg discord.gg/custom_url_yeet

    {{param}} max_presences [int]
        Maximum number of statuses, like "Playing a game lol"

    {{param}} embed_enabled [bool]
        Whether or not the guild embed has been enabled

    {{param}} premium_tier [int]
        Boost level of the server

    {{param}} embed_channel_id [str, ~/Snow, int]
        The embed channel ID, if the embed is enabled

    {{param}} joined_at [str]
        A standard ISO 8601 timestamp indicating when the client joined the
        guild

    {{param}} large [bool]
        Whether or not the guild is considered "large"... ask Discord

    {{param}} widget_channel_id [str, ~/Snow, int]
        The ID of the widget channel

    {{param}} widget_enabled [bool]
        Whether or not the widget is enabled

    {{param}} unavailable [bool]
        Whether or not the guild is offline

    {{param}} member_count [int]
        Number of players in the guild

    {{param}} members [List[dict]]
        A list of dict players in the guild

    {{param}} voice_states [List[dict]]
        A list of voice states

    {{param}} channels [List[dict]]
        A list of dict channels in the guild. Will automatically be formed into
        their respective objects eg a voice channel will be created as a VC

    {{param}} presences [List[dict]]
        A list of statuses

    {{param}} max_members [int]
        How many players this guild can have

    {{param}} premium_subscription_count [int]
        How many players are currently boosting the guild

    {{param}} lazy [bool]
        I don't know, discord doesn't document it

    {{param}} bot_obj [~/Bot]
        The bot object... because I want to make sure you can access the bot
        from anywhere within your code... arhem d.py

    {{prop}} id [int]
        ID of the guild

    {{prop}} name [str]
        Name of the guild

    {{prop}} icon_hash [str]
    {{prop}} splash_hash [str]
    {{prop}} banner_hash [str]
    {{prop}} discovery_splash_hash [str]
        Hashes of assets

    {{prop}} icon [str]
    {{prop}} splash [str]
    {{prop}} banner [str]
    {{prop}} discovery_splash [str]
        URLs instead of hashes, useful if you want to download the file or
        upload it

    {{prop}} afk_vc_id [int]
    {{prop}} system_channel_id [int]
    {{prop}} embed_channel_id [int]
    {{prop}} widget_channel_id [int]
    {{prop}} rules_channel_id [int]
        The special guild channel IDs, all names are self explanitory

    {{prop}} afk_vc [~/Channel.AnyChannel]
    {{prop}} system_channel [~/Channel.AnyChannel]
    {{prop}} embed_channel [~/Channel.AnyChannel]
    {{prop}} widget_channel [~/Channel.AnyChannel]
    {{prop}} rules_channel [~/Channel.AnyChannel]
        The special guild channels, all names are self explanitory

    {{prop}} is_owner [bool]
        Whether or not the client is the owner of the guild
    """
    def __init__(self, *, id, name, icon, splash, owner_id, region,
                 afk_channel_id, afk_timeout, verification_level,
                 default_message_notifications, explicit_content_filter,
                 mfa_level, application_id, system_channel_id, rules_channel_id,
                 vanity_url_code, description = "", preferred_locale = "",
                 banner = "", discovery_splash = "", roles = [], owner = False,
                 permissions = 0, max_presences = 0, embed_enabled = False,
                 premium_tier = 0, emojis = [], embed_channel_id = None,
                 widget_enabled = False, features = [], joined_at = None,
                 widget_channel_id = None, large = False, unavailable = False,
                 member_count = 0, members = [], voice_states = [],
                 channels = [], presences = [], max_members = 0, lazy = False,
                 premium_subscription_count = 0, system_channel_flags = 0,
                 bot_obj = None):
        self.id = int(id)
        self.name = str(name)

        #Assets
        self.icon_hash = icon
        self.splash_hash = splash
        self.banner_hash = banner
        self.discovery_splash_hash = discovery_splash

        #Channels
        self.afk_vc_id = int(afk_channel_id or 0)
        self.system_channel_id = int(system_channel_id or 0)
        self.embed_channel_id = int(embed_channel_id or 0)
        self.widget_channel_id = int(widget_channel_id or 0)
        self.rules_channel_id = int(rules_channel_id or 0)

        #Lists
        bot_obj.raw_many(
            [
                ["roles", roles],
                ["emojis", emojis],
                ["players", members],
                ["channels", channels],
            ],
            bot_obj = bot_obj,
            guild_id = id
        )

        #Metadata
        self.region = region[0]
        self.afk_timeout = int(afk_timeout)
        self.has_embed = embed_enabled
        self.features = features
        self.mfa_level = mfa_level
        self.app_id = application_id
        self.has_widget = widget_enabled
        self.boost_level = premium_tier
        self.boosters = premium_subscription_count

        #Other
        self.is_owner = owner
        self.owner_id = int(owner_id)
        self.perms = Perms(permissions)
        self.verify_level = int(verification_level)
        self.default_message_notifs = default_message_notifications
        self.nsfw_filter = int(explicit_content_filter)
        self.joined = from_ts(joined_at)
        self.large = large
        self.out = unavailable
        self.player_count = member_count
        self.voice_states = voice_states
        self.locale = preferred_locale
        self.bot_obj = bot_obj

    async def make_channel(self, name: str, *, topic: str = "", overwrites = [],
                           slowmode: int = 0, nsfw: bool = False,
                           category = None):
        """
        {{loc}} discord.models.Channel
        {{fn}} await instance.make_channel(name, *, topic, overwrites, slowmode,
        nsfw, category)

        {{desc}} Creates a text channel

        {{param}} name [str]
            The name of the new channel

        {{param}} topic [str]
            Topic of the new channel
            {{norm}} ""

        {{param}} overwrites [List[dict, ~/Perms/Overwrite], ~/Perms/Overwrites]
            Channel overwrites
            {{norm}} []

        {{param}} slowmode [int]
            The slowmode limit in seconds
            {{norm}} 0

        {{param}} nsfw [bool]
            Whether or not this channel is NSFW
            {{norm}} False

        {{param}} category [int, str, ~.Category]
            The category this channel belongs to
            If int, then it must be the ID
            If str, then it must be the name or ID
            If ~.Category, then it must be in this guild
            If None, then it means that there is no category
            {{norm}} None

        {{rtn}} [~.Channel] The new channel
        """
        pID = id_from_obj(category, self.categories, "Category")
        d = {
            "name": name,
            "topic": topic,
            "type": 0,
            "parent_id": pID,
            "permission_overwrites": [dict(ovw) for ovw in overwrites],
            "rate_limit_per_user": slowmode,
            "nsfw": nsfw
        }
        obj = await self.bot_obj.http.make_channel(
            self.guild_id, d, bot_obj = self.bot_obj, guild_id = self.guild
        )
        return self.bot_obj.all_channels(obj.id)

    async def make_store(self, name: str, *, topic: str = "", overwrites = [],
                         slowmode: int = 0, nsfw: bool = False,
                         category = None):
        """
        {{fn}} await instance.make_store(name, *, topic, overwrites, slowmode,
        nsfw, category)

        {{desc}} Creates a store channel under this category

        {{param}} name [str]
            The name of the new channel

        {{param}} topic [str]
            Topic of the new channel
            {{norm}} ""

        {{param}} overwrites [List[dict, ~/Perms/Overwrite], ~/Perms/Overwrites]
            Channel overwrites
            {{norm}} []

        {{param}} slowmode [int]
            The slowmode limit in seconds
            {{norm}} 0

        {{param}} nsfw [bool]
            Whether or not this channel is NSFW
            {{norm}} False

        {{param}} category [int, str, ~.Category]
            The category this channel belongs to
            If int, then it must be the ID
            If str, then it must be the name or ID
            If ~.Category, then it must be in this guild
            If None, then it means that there is no category
            {{norm}} None

        {{rtn}} [~.StoreChannel] The new channel
        """
        pID = id_from_obj(category, self.categories, "Category")
        d = {
            "name": name,
            "topic": topic,
            "type": 6,
            "parent_id": pID,
            "permission_overwrites": [dict(ovw) for ovw in overwrites],
            "rate_limit_per_user": slowmode,
            "nsfw": nsfw
        }
        obj = await self.bot_obj.http.make_channel(
            self.guild_id, d, bot_obj = self.bot_obj, guild_id = self.guild
        )
        return self.bot_obj.all_channels(obj.id)

    async def make_news(self, name: str, *, topic: str = "", overwrites = [],
                        slowmode: int = 0, nsfw: bool = False, category = None):
        """
        {{fn}} await instance.make_news(name, *, topic, overwrites, slowmode,
        nsfw, category)

        {{desc}} Creates a news channel under this category

        {{param}} name [str]
            The name of the new channel

        {{param}} topic [str]
            Topic of the new channel
            {{norm}} ""

        {{param}} overwrites [List[dict, ~/Perms/Overwrite], ~/Perms/Overwrites]
            Channel overwrites
            {{norm}} []

        {{param}} slowmode [int]
            The slowmode limit in seconds
            {{norm}} 0

        {{param}} nsfw [bool]
            Whether or not this channel is NSFW
            {{norm}} False

        {{param}} category [int, str, ~.Category]
            The category this channel belongs to
            If int, then it must be the ID
            If str, then it must be the name or ID
            If ~.Category, then it must be in this guild
            If None, then it means that there is no category
            {{norm}} None

        {{rtn}} [~.NewsChannel] The new channel
        """
        pID = id_from_obj(category, self.categories, "Category")
        d = {
            "name": name,
            "topic": topic,
            "type": 5,
            "parent_id": pID,
            "permission_overwrites": [dict(ovw) for ovw in overwrites],
            "rate_limit_per_user": slowmode,
            "nsfw": nsfw
        }
        obj = await self.bot_obj.http.make_channel(
            self.guild_id, d, bot_obj = self.bot_obj, guild_id = self.guild
        )
        return self.bot_obj.all_channels(obj.id)

    async def make_vc(self, name: str, *, bitrate: int = 64, overwrites = [],
                      limit: int = 0, category = None):
        """
        {{fn}} await instance.make_vc(name, *, bitrate, overwrites, limit,
        category)

        {{desc}} Creates a voice channel under this category

        {{param}} name [str]
            The name of the new vc

        {{param}} bitrate [int]
            The bitrate of this vc
            {{norm}} 64

        {{param}} overwrites [List[dict, ~/Perms/Overwrite], ~/Perms/Overwrites]
            Channel overwrites

        {{param}} limit [int]
            Number of users this vc can hold
            {{norm}} 0

        {{param}} category [int, str, ~.Category]
            The category this channel belongs to
            If int, then it must be the ID
            If str, then it must be the name or ID
            If ~.Category, then it must be in this guild
            If None, then it means that there is no category
            {{norm}} None

        {{rtn}} [~.VC] The new channel
        """
        pID = id_from_obj(category, self.categories, "Category")
        d = {
            "name": name,
            "type": 2,
            "parent_id": pID,
            "permission_overwrites": [dict(ovw) for ovw in overwrites],
            "bitrate": bitrate,
            "user_limit": limit
        }
        obj = await self.bot_obj.http.make_channel(
            self.guild_id, d, bot_obj = self.bot_obj, guild_id = self.guild
        )
        return self.bot_obj.all_channels(obj.id)

    def __dict__(self):
        """
        {{bltin}} instance.__dict__()
        {{usage}} dict(instance)

        {{pydesc}} __dict__

        {{rtn}} [dict]
        """
        return {
            "id": str(self.id),
        }

    #Named Aliases
    @property
    def owner(self):
        return self.players(self.owner_id)

    @property
    def icon(self):
        return Url.guild_icon(self.id, self.icon_hash)

    @property
    def splash(self):
        return Url.guild_splash(self.id, self.splash_hash)

    @property
    def banner(self):
        return Url.guild_banner(self.id, self.banner_hash)

    @property
    def discovery_splash(self):
        return Url.guild_discovery(self.id, self.discovery_splash_hash)

    @property
    def embed_channel(self):
        if self.embed_channel_id:
            return self.bot_objs.all_channels(self.embed_channel_id)
        return None

    @property
    def afk_vc(self):
        if self.afk_vc_id:
            return self.bot_objs.all_channels(self.afk_vc_id)
        return None

    @property
    def widget_channel(self):
        if self.widget_channel_id:
            return self.bot_objs.all_channels(self.widget_channel_id)
        return None

    @property
    def rules_channel(self):
        if self.rules_channel_id:
            return self.bot_objs.all_channels(self.rules_channel_id)
        return None

    @property
    def system_channel(self):
        if self.system_channel_id:
            return self.bot_objs.all_channels(self.system_channel_id)
        return None

    @property
    def players(self):
        dic = PrizmDict()
        for player in self.bot_obj.players:
            if player.guild_id == self.id:
                dic[player.id] = player
        return dic

    @property
    def roles(self):
        dic = PrizmDict()
        for role in self.bot_obj.roles:
            if role.guild_id == self.id:
                dic[role.id] = role
        return dic

    @property
    def emojis(self):
        dic = PrizmDict()
        for emoji in self.bot_obj.emojis:
            if emoji.guild_id == self.id:
                dic[emoji.id] = emoji
        return dic

    def channels_by_type(self, typ = None):
        dic = PrizmDict()
        ls = []
        if typ == None:
            ls = self.bot_obj.all_channels
        elif typ == 0:
            ls = self.bot_obj.channels
        elif typ == 2:
            ls = self.bot_obj.vcs
        elif typ == 5:
            ls = self.bot_obj.news_channels
        elif typ == 6:
            ls = self.bot_obj.store_channels
        elif typ == 4:
            ls = self.bot_obj.categories
        for channel in ls:
            if channel.guild_id == self.id:
                dic[channel.id] = channel
        return dic

    @property
    def all_channels(self):
        return self.channels_by_type()

    @property
    def channels(self):
        return self.channels_by_type(0)

    @property
    def vcs(self):
        return self.channels_by_type(2)

    @property
    def categories(self):
        return self.channels_by_type(4)

    @property
    def news_channels(self):
        return self.channels_by_type(5)

    @property
    def store_channels(self):
        return self.channels_by_type(6)
