import datetime
from .Snow import Snow
from .Player import Player
from .Member import Member
from .Reaction import Reaction
from .Raw import Raw
from .Guild import Guild
from .Channel import Channel, VoiceChannel, Catagory,

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
                 flags: int = 0, bot):
        self.id = int(id)
        self.channel_id = int(channel_id)
        self.guild_id = None
        if guild_id != None:
            self.guild_id = Raw(guild_id, "/guilds/{id}", bot)
        self.author = member or author
        self.text = content
        self.time = datetime.datetime.fromisoformat(timestamp)
        self.edited = bool(edited_timestamp)
        self.edited_at = datetime.datetime.fromisoformat(edited_timestamp) if edited_timestamp else None
        self.tts = tts
        self.at_everyone = mention_everyone
        self.mentions = [int(mID) for mID in mentions]
        self.pinned = pinned
        self.role_mentions = [
        self.channel_mentions = [int(cID) for cID in mention_channels]
        self.reactions = [Reaction(