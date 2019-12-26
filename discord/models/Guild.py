from .Raw import RawFile, RawObj, RawObjs, Raw
from .Role import Role
from .Channel import AnyChannel
from .Emoji import Emoji
from . import Url
from .Member import Player
from .Perms import Perms
from .Voice import VoiceRegion
from .ClsUtil import from_ts

__all__ = ["Guild"]

class Guild:
    """
    {{cls}} instance = Guild(*, too_many_args_to_list_here)

    {{desc}} Represents a Guild

    {{note}} This class shouldn't be initialized by hand. Don't do that.

    {{note}} A "guild" is referred to as a "server" in the UI

    {{param}} id [str, discord.models.Snow]
        The guild ID

    {{param}} name [str]
        The name of the guild

    {{param}} splash [str]
        Hash of the splash image

    {{param}} owner_id [str, discord.models.Snow]
        ID of the owner

    {{param}} region [str]
        Voice region of the guild

    {{param}} features [List[str]]
        A list of features available to the guild

    {{param}} afk_channel_id [str, discord.models.Snow]
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

    {{param}} application_id [str, discord.models.Snow]
        The app id of the bot that created the server, None if it wasn't made by
        a bot

    {{param}} system_channel_id [str, discord.models.Snow]
        The channel ID of welcome messages, boost messages, and more

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

    {{param}} embed_channel_id [str, discord.models.Snow]
        The embed channel ID, if the embed is enabled

    {{param}} joined_at [str]
        A standard ISO 8601 timestamp indicating when the client joined the
        guild

    {{param}} large [bool]
        Whether or not the guild is considered "large"... ask Discord

    {{param}} widget_channel_id [str, discord.models.Snow]
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

    {{param}} bot_obj [discord.models.Bot]
        The bot object... because I want to make sure you can access the bot
        from anywhere within your code... arhem d.py

    {{prop}} id [int]
        ID of the guild

    {{prop}} name [str]
        Name of the guild

    {{prop}} icon_hash [str]
        Icon hash

    {{prop}} icon [str]
        The URL of the icon

    {{prop}} icon_file [discord.models.Raw.RawFile]
        The RawFile

    {{prop}} splash_hash [str]
        Splash hash

    {{prop}} splash [str]
        URL of the splash

    {{prop}} splash_file [discord.models.Raw.RawFile]
        The RawFile

    {{prop}} banner_hash [str]
        Banner hash

    {{prop}} banner [str]
        URL of the banner

    {{prop}} banner_file [discord.models.Raw.RawFile]
        The RawFile

    {{prop}} afk_vc_id [int]
        The AFK VC ID

    {{prop}} afk_vc [None, discord.models.Channel.VC]
        The AFK VC... or None of it doesn't actually exist

    {{prop}} system_channel_id [int]
        The system channel of the guild, for welcome and boost messages and more

    {{prop}} system_channel [None, discord.models.Channel.Channel]
        The system channel, or None if it doesn't actually exist

    {{prop}} embed_channel_id [int]
        The embed channel ID

    {{prop}} embed_channel [None, discord.models.Channel.AnyChannel]
        The embed channel

    {{prop}} widget_channel_id [int]
        The widget channel ID

    {{prop}} widget_channel [None, discord.models.Channel.AnyChannel]
        The widget channel

    {{prop}} roles [List[discord.models.Role]]
        The list of roles the guild owns

    {{prop}} emojis [List[discord.models.Emoji]]
        The list of emojis the guild owns

    {{prop}} players [List[discord.models.Member.Player]]
        The list of players the guild has

    {{prop}} channels [List[discord.models.Channel.AnyChannel]]
        The list of channels the guild owns

    {{prop}} region [discord.models.Voice.VoiceRegion]
        The voice region

    {{prop}} afk_timeout [int]
        The AFK timeout

    {{prop}} has_embed [bool]
        Whether or not the embed has been enabled

    {{prop}} features [List[str]]
        A list of features the guild has access to

    {{prop}} mfa_level [int]
        The 2FA level

    {{prop}} app_id [int]
        ID of the bot that made the guild, 0 if it was made by a human

    {{prop}} has_widget [bool]
        Whether or not the guild has a widget

    {{prop}} boost_level [int]
        The boost level of the guild

    {{prop}} boosters [int]
        How many people are currently boosting the guild

    {{prop}} owner_id [int]
        The ID of the owner

    {{prop}} is_owner [bool]
        Whether or not the client owns the guild

    {{prop}} owner [discord.models.Member.Player]
        Who actually owns the guild

    {{prop}} perms [discord.models.Perms.Perms]
        The permission level for the client

    {{prop}} verify_level [int]
        The level of verification

    {{prop}} default_message_notifs [int]
        The default message notification level

    {{prop}} nsfw_filter [int]
        The level of NSFW filtering

    {{prop}} joined [datetime.datetime]
        When the client joined the server

    {{prop}} large [bool]
        Whether or not the guild is large

    {{prop}} out [bool]
        Whether or not the guild is offline

    {{prop}} player_count [int]
        Number of players in the guild

    {{prop}} voice_states [List[dict]]
        List of voice states

    {{prop}} locale [str]
        Default language

    {{prop}} bot_obj [discord.models.Bot]
        The bot object
    """
    def __init__(self, *, id, name, icon, splash, owner_id, region,
                 afk_channel_id, afk_timeout, verification_level,
                 default_message_notifications, explicit_content_filter,
                 mfa_level, application_id, system_channel_id, vanity_url_code,
                 description = "", preferred_locale = "", banner = "",
                 roles = [], owner = False, permissions = 0, max_presences = 0,
                 embed_enabled = False, premium_tier = 0, emojis = [],
                 embed_channel_id = None, widget_enabled = False, features = [],
                 widget_channel_id = None, joined_at = None, large = False,
                 unavailable = False, member_count = 0, members = [],
                 voice_states = [], channels = [], presences = [],
                 max_members = 0, premium_subscription_count = 0,
                 bot_obj = None):
        self.id = int(id)
        self.name = str(name)

        #Assets
        self.icon_hash = icon
        self.icon = Url.guild_icon(id, icon)
        self.icon_file = RawFile(self.icon)
        self.splash_hash = splash
        self.splash = Url.guild_splash(id, splash)
        self.splash_file = RawFile(self.splash)
        self.banner_hash = banner
        self.banner = Url.guild_banner(id, banner)
        self.banner_file = RawFile(self.banner)

        #Channels
        self.afk_vc_id = int(afk_channel_id)
        self.system_channel_id = int(system_channel_id)
        self.embed_channel_id = int(embed_channel_id)
        self.widget_channel_id = int(widget_channel_id)
        self.afk_vc = None
        self.system_channel = None
        self.embed_channel = None
        self.widget_channel = None

        #Lists
        self.roles = bot_obj.raw(
            "roles", roles, bot_obj = bot_obj
        )
        self.emojis = bot_obj.raw(
            "emojis", emojis, bot_obj = bot_obj, guild_id = id
        )
        self.players = bot_obj.raw(
            "players", members, bot_obj = bot_obj
        )
        self.channels = bot_obj.raw(
            "channels", channels, bot_obj = bot_obj
        )
        #self.presences = bot_obj.raw(
        #^idk yet

        if afk_channel_id:
            self.afk_vc = bot_obj.listeners.channels(afk_channel_id)
        if embed_channel_id:
            self.embed_channel = bot_obj.listeners.channels(embed_channel_id)
        if widget_channel_id:
            self.widget_channel = bot_obj.listeners.channels(widget_channel_id)
        if system_channel_id:
            self.system_channel = bot_obj.listeners.channels(system_channel_id)

        #Metadata
        self.region = VoiceRegion(region)
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
        self.owner = bot_obj.listeners.players(owner_id)
        self.perms = Perms(permissions, 0, 0)
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
