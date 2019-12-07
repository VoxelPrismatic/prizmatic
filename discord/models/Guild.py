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
    DESCRIPTION ---
        Represents a Guild

    PARAMS ---
        This class shouldn't be initialized by hand. Don't do that.

    FUNCTIONS ---
        None yet
    """

    def __init__(self, *, id, name, icon, splash, owner_id, region, afk_channel_id,
                 afk_timeout, verification_level, default_message_notifications,
                 explicit_content_filter, roles, emojis, features, mfa_level,
                 application_id, system_channel_id, vanity_url_code, description,
                 banner, premium_tier, preferred_locale, owner = False,
                 permissions = 0, embed_enabled = False, embed_channel_id = None,
                 widget_enabled = False, widget_channel_id = None, joined_at = None,
                 large = False, unavailable = False, member_count = 0, members = [],
                 voice_states = [], channels = [], presences = [], max_presences = 0,
                 max_members = 0, premium_subscription_count = 0, bot_obj = None):
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
        if afk_channel_id:
            self.afk_vc = bot_obj.find_list("channels", afk_channel_id)
        if embed_channel_id:
            self.embed_channel = bot_obj.find_list("channels", embed_channel_id)
        if widget_channel_id:
            self.widget_channel = bot_obj.find_list("channels", widget_channel_id)
        if system_channel_id:
            self.system_channel = bot_obj.find_list("channels", system_channel_id)

        #Lists
        self.roles = bot_obj.raw("roles", roles, bot_obj = bot_obj)
        self.emojis = bot_obj.raw("emojis", emojis, bot_obj = bot_obj, guild_id = id)
        self.members = bot_obj.raw("players", members, bot_obj = bot_obj)
        self.channels = bot_obj.raw("channels", channels, bot_obj = bot_obj)
        #self.presences = bot_obj.raw(
        #^idk yet

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
        self.owner_id = int(owner_id)
        self.owner = bot_obj.find("players", owner_id,
                                  f"/guilds/{id}/members/{owner_id}", bot_obj = bot_obj)
        self.perms = Perms(permissions, 0, 0)
        self.verify_level = int(verification_level)
        self.default_message_notifs = default_message_notifications
        self.nsfw_filter = int(explicit_content_filter)
        self.joined = from_ts(joined_at)
        self.large = large
        self.out = unavailable
        self.member_count = member_count
        self.voice_states = voice_states
        self.locale = preferred_locale
        self.bot_obj = bot_obj
