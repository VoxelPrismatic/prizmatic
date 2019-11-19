class Party:
    """
    DESCRIPTION ---
        Represents a party
        
    PARAMS ---
        This class shouldn't be initialized by hand. Don't do that.
        
    FUNCTIONS ---
        None yet
    """
    def __init__(self, id, size):
        self.id = id
        self.size = size
    def __dict__(self):
        return {"id": self.id, "size": self.size}