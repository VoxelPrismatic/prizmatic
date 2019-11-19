from .Raw import RawFile, RawObj, RawObjs, Raw
from .Role import Role
from .Channel import VC, Channel, AnyChannel
from .Emoji import Emoji
from .Url import Url
from .Player import Player
from .Perms import Perms
import datetime

class Guild:
    """
    DESCRIPTION ---
        Represents a Guild
        
    PARAMS ---
        This class shouldn't be initialized by hand. Don't do that.
        
    FUNCTIONS ---
        None yet
    """

    def __init__(self, *, id, name, icon, splash, owner = False, owner_id, 
                 permissions = 0, region, afk_channel_id, afk_timeout, 
                 embed_enabled = False, embed_channel_id = 0, verification_level,
                 default_message_notifications, explicit_content_filter, roles = [], 
                 emojis = [], features = [], mfa_level, appliction_id = None, 
                 widget_enabled = False, widget_channel_id = 0, system_channel_id, 
                 joined_at = "1970-01-01T00:00:00+00:00", large = False, unavailable,
                 member_count, voice_states, members, channels, presences, 
                 max_presences, max_members, vanity_url_code, description, banner, 
                 premium_teir, premium_subscription_count, preffered_locale, bot_obj):
        self.id = int(id)
        self.name = name
        self.icon_hash = icon
        self.icon = Url.guild_icon(id, icon)
        self.icon_file = RawFile(self.icon)
        self.splash_hash = splash
        self.splash = Url.guild_splash(id, splash)
        self.splash_file = RawFile(self.splash)
        self.banner_hash = banner
        self.banner = Url.guild_banner(id, banner)
        self.banner_file = RawFile(self.banner)
        self.owner_id = int(owner_id)
        self.perms = Perms(permissions, 0, 0)
        self.roles = RawObjs(Role, roles, bot_obj = bot_obj)
        self.region = region
        self.afk_vc_id = int(afk_channel_id)
        self.afk_timeout = int(afk_timeout)
        self.has_embed = embed_enabled
        self.embed_channel_id = int(embed_channel_id)
        self.verify_level = int(verification_level)
        self.default_message_notifs = default_message_notifications
        self.nsfw_filter = int(explicit_content_filter)
        self.emojis = RawObjs(Emoji, emojis, bot_obj = bot_obj)
        self.features = features
        self.mfa_level = mfa_level
        self.app_id = application_id
        self.has_widget = widget_enabled
        self.widget_channel_id = int(widget_channel_id)
        self.widget_channel = Raw(AnyChannel, widget_channel_id, "/channels/{id}", 
                                  bot_obj = bot_obj)
        self.system_channel_id = int(system_channel_id)
        self.system_channel = Raw(AnyChannel, system_channel_id, "/channels/{id}", 
                                  bot_obj = bot_obj)
        self.joined = datetime.datetime.fromtimestamp(joined_at)
        self.large = large
        self.out = unavailable
        self.member_count = member_count
        self.voice_states = voice_states
        self.members = RawObjs(Player, members, bot_obj = bot_obj)
        self.channels = RawObjs(AnyChannel, channels, bot_obj = bot_obj)
        self.presences = None