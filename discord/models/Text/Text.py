from ..ClsUtil import from_ts
from ..Snow import Snow
from ..Member import Player
from ..Reaction import Reaction
from ..Raw import Raw
from ..Channel import AnyChannel

__all__ = ["Text"]

class Text:
    """
    DESCRIPTION ---
        Represents a message

    PARAMS ---
        This class shouldn't be initialized by hand. Don't do that.

    FUNCTIONS ---
        None yet
    """
    def __init__(self, *, id, channel_id, guild_id = None, author, member = None,
                 content: str, timestamp, edited_timestamp = None, tts: bool,
                 mention_everyone: bool, mentions = [], pinned: bool,
                 mention_roles = [], mention_channels = [], attachments, embeds,
                 reactions = [], nonce, webhook_id = None, type: int,
                 activity = None, application = None, message_reference = None,
                 flags: int = 0, bot_obj = None):
        self.id = int(id)
        self.channel_id = int(channel_id)
        self.guild_id = None
        if guild_id != None:
            self.guild_id = bot_obj.listeners.guilds(guild_id)
        self.author = member or author
        self.text = content
        self.time = from_ts(timestamp)
        self.edited = bool(edited_timestamp)
        self.edited_at = None
        if self.edited:
            self.edited_at = from_ts(edited_timestamp)
        self.tts = tts
        self.at_everyone = mention_everyone
        self.mentions = [int(mID) for mID in mentions]
        self.pinned = pinned
        self.role_mentions = []
        self.channel_mentions = [int(cID) for cID in mention_channels]
        #self.reactions = [Reaction(
