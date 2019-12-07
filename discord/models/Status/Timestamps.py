from ..ClsUtil import from_ts

__all__ = ["Timestamps"]

class Timestamps:
    """
    DESCRIPTION ---
        Represents timestamps

    PARAMS ---
        This class shouldn't be initialized by hand. Don't do that.

    FUNCTIONS ---
        None yet
    """
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __dict__(self):
        return {"start": self.start, "end": self.end}
