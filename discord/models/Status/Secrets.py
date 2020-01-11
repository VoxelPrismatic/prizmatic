__all__ = ["Secrets"]

class Secrets:
    """
    {{cls}} instance = Secrets(*, join, spectate, match)

    {{note}} This class shouldn't be initialized by hand. Don't do that.

    {{desc}} Represents secrets

    {{param}} join [str]
        The secrets to join the game

    {{param}} spectate [str]
        The secrets to spectate the game

    {{param}} match [str]
        The secrets to make a match in the game

    {{prop}} join [str]
        The secrets to join the game

    {{prop}} spectate [str]
        The secrets to spectate the game

    {{prop}} match [str]
        The secrets to make a match in the game
    """
    def __init__(self, join, spectate, match):
        self.join = join
        self.spectate = spectate
        self.match = match

    def __dict__(self):
        """
        {{bltin}} instance.__dict__()
        {{usage}} dict(instance)

        {{pydesc}} __dict__

        {{rtn}} [dict]
        """
        return {
            "join": self.join, "spectate": self.spectate, "match": self.match
        }
