from datetime.datetime import fromtimestamp as from_ts
from ..Member import User

class InviteMetadata:
    """
    DESCRIPTION ---
        Represents invite metadata
    
    PARAMS ---
        This class shouldn't be initialized by hand. Don't do that.
    
    FUNCTIONS ---
        meta = InviteMetadata(inviter, uses, max_uses, max_age, temp, made)
        - Created a new InviteMetadata object
    """
    def __init__(self, inviter, uses, max_uses, max_age, temporary, created_at):
        self.inviter = User(**inviter)
        self.uses = uses
        self.max_uses = max_uses
        self.max_age = max_age
        self.temp = temporary
        self.made_at = from_ts(created_at)