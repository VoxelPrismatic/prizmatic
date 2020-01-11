from ..ClsUtil import from_ts
from ..Snow import Snow
from ..Member import Player
from ..Reaction import Reaction
from ..Raw import Raw
from ..Channel import AnyChannel

__all__ = ["Text"]

class Text:
    """
    {{cls}} instance = Text(*, too_many_args_to_list_here)

    {{desc}} Represents a message

    {{noinit}}

    {{note}} The documentation for this class is not complete yet

    {{param}} id [str, ~/Snow]
        ID of the message

    {{param}} channel_id [str, ~/Snow]
        The Channel ID

    {{param}} guild_id [str, ~/Snow, None]
        The Guild ID, or None if it is in DMs

    {{param}} content [str]
        The content of the message

    {{param}} member [~/Member.Player, ~/Member.User]
        The player or user that sent the message. If a user, then the user
        either left the guild or sent the message in DMs.

    {{param}} timestamp [str]
        When this channel was made
    """
    def __init__(self, *, id, channel_id, author, member = None,
                 content: str, timestamp, edited_timestamp = None, tts: bool,
                 mention_everyone: bool, pinned: bool, type: int, mentions = [],
                 guild_id = None, mention_roles = [], mention_channels = [],
                 attachments, embeds, reactions = [], nonce, webhook_id = None,
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
