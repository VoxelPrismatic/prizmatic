from .PrizmCls import *
from .Color import Color
from .Perms import Perms

class Role:
    """
    DESCRIPTION ---
        Represents a role
        
    PARAMS ---
        This class shouldn't be initialized by hand. Don't do that.
        
    FUNCTIONS ---
        None yet
    """
    def __init__(self, id, name, color, hoist,
                 position, permissions, managed,
                 mentionable):
        self.name = name
        self.color = Color(color)
        self.hoist = hoist
        self.position = position
        self.perms = Perms(permissions)
        self.managed = managed
        self.mentionable = mentionable