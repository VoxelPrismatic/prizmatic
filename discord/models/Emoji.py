from .Role import Role
from .Raw import RawObjs, RawFile
from .Member import User
from .Url import Url

class Emoji:
    """
    DESCRIPTION ---
        Represents an emoji
    
    PARAMS ---
        This class shouldn't be initialized by hand. Don't do that.
    
    FUNCTIONS ---
        emoji = Emoji(id, name, roles, user, colons, managed, animated)
        - Creates an Emoji object
    """
    def __init__(self, id, name, roles, user, require_colons = False,
                 managed = False, animated = False, bot_obj = None):
        self.id = id
        self.name = name
        self.roles = RawObjs(Role, roles)
        self.user = User(**user)
        self.colons = require_colons
        self.gif = animated
        self.managed = managed
        self.url = Url.emoji(id)
        self.file = RawFile(self.url, bot_obj)
        self.bot_obj = bot_obj
    
    def __str__(self):
        if self.id:
            c = ""
            a = ""
            if self.colons:
                c = ":"
            if self.gif:
                a = "a"
            return f"<{a}{c}{self.id}{c}{self.name}>"
        return self.name
    
    def __repr__(self):
        pre = "Twemoji"
        if self.id:
            pre = "Custom Emoji"
        if self.gif:
            pre = "Animated Custom Emoji"
        return f"<{pre} '{self.name}'>"
    