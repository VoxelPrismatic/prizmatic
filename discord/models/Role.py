from .PrizmCls import *
from .Color import Color
from .Perms import Perms

class Role:
    """
    Represents a role
    **You shouldn't have to initialize this class, so no documentation for
      initializing this class will be given
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