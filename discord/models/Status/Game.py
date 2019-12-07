from .Timestamps import Timestamps
from .Party import Party
from .Secrets import Secrets
from .Assets import Assets

__all__ = ["Game"]

class Game:
    """
    DESCRIPTION ---
        Represents a game

    PARAMS ---
        This class shouldn't be initialized by hand. Don't do that.

    FUNCTIONS ---
        None yet
    """
    def __init__(self, name, type, url, timestamps, application_id, details,
                 state, party = None, assets = None, secrets = None, instance = None,
                 flags = 0, bot_obj = None):
        self.name = name
        if str(type).lower() in ["0", "game", "playing"]:
            self.type = 0
        elif str(type).lower() in ["1", "stream", "streaming", "twitch"]:
            self.type = 1
        elif str(type).lower() in ["2", "listening to", "music", "listen"]:
            self.type = 2
        self.url = url
        self.timestamps = Timestamps(**timestamps)
        self.app_id = application_id
        self.details = details
        self.state = state
        self.party = Party(**party)
        self.assets = Assets(**assets)
        self.secrets = Secrets(**secrets)
        self.bot_obj = bot_obj
