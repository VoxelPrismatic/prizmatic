from .Timestamps import Timestamps
from .Party import Party
from .Secrets import Secrets
from .Assets import Assets

__all__ = ["Game"]

class Game:
    """
    {{cls}} instance = Game(*, too_many_args_to_list_here)

    {{note}} This class shouldn't be initialized by hand. Don't do that.

    {{desc}} Represents a game or activity

    {{param}} name [str]
        The name of the GPA

    {{param}} url [str]
        The optional URL

    {{param}} timestamps [dict, discord.models.Status.Timestamps]
        A timestamps object representing the start and end times

    {{param}} application_id [str]
        The game ID

    {{param}} details [str]
        Other things that discord sent

    {{param}} state [str]
        The state of the game

    {{param}} party [dict, discord.models.Status.Party]
        A party object

    {{param}} assets [dict, discord.models.Status.Assets]
        An assets object

    {{param}} secrets [dict, discord.models.Status.Secrets]
        A secrets object

    {{param}} instance [bool]
        Whether or not the game is instanced

    {{param}} flags [int]
        Additional flags

    {{param}} bot_obj [discord.models.Bot]
        The bot object

    {{prop}} name [str]
        The name of the GPA

    {{prop}} url [str]
        The optional URL

    {{prop}} timestamps [dict, discord.models.Status.Timestamps]
        A timestamps object representing the start and end times

    {{prop}} app_id [str]
        The game ID

    {{prop}} details [str]
        Other things that discord sent

    {{prop}} state [str]
        The state of the game

    {{prop}} party [dict, discord.models.Status.Party]
        A party object

    {{prop}} assets [dict, discord.models.Status.Assets]
        An assets object

    {{prop}} secrets [dict, discord.models.Status.Secrets]
        A secrets object

    {{prop}} instance [bool]
        Whether or not the game is instanced

    {{prop}} flags [int]
        Additional flags

    {{prop}} bot_obj [discord.models.Bot]
        The bot object
    """
    def __init__(self, name, type, url, timestamps, application_id, details,
                 state, party = None, assets = None, secrets = None,
                 instance = None, flags = 0, bot_obj = None):
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

    def __dict__(self):
        """
        {{bltin}} instance.__dict__()
        {{usage}} dict(instance)

        {{pydesc}} __dict__

        {{rtn}} [dict]
        """
