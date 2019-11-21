from .Perms import Perms
from ..Snow import Snow

class Overwrite:
    """
    DESCRIPTION ---
        Represents a permission overwrite
    
    PARAMS ---
        This class shouldn't be initialized by hand. Don't do that.
        
    FUNCTIONS ---
        overwrite = Overwrite(id, type, allow_int, deny_int)
        - Create an Overwrite object, don't do this.
        
        overwrite.update(allow_int, deny_int)
        - Updates the overwrites. Use perms.encode() if you want.
        
        dict(overwrite)
        - Used internally to prepare the object for sending
    """
    def __init__(self, *, id, type, allow_int, deny_int):
        self.id = Snow(id)
        self.type = type
        self.perms = Perms(allow = allow_int, deny = deny_int)
        
    def update(self, allow_int = None, deny_int = None):
        if allow_int is None:
            allow_int = self.perms.allow_int
        if deny_int is None:
            deny_int = self.perms.deny_int
        self.perms.update_int(allow = allow_int, deny = deny_int)
    
    def __dict__(self):
        return {
            "type": self.type,
            "allow": self.perms.allow_int,
            "deny": self.perms.deny_int
        }