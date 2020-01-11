__all__ = ["Party"]

class Party:
    """
    {{cls}} instance = Party(*, id, size)

    {{note}} This class shouldn't be initialized by hand. Don't do that.

    {{desc}} Represents a party

    {{param}} id [str, discord.models.Snow]
        The ID of the party

    {{param}} size [int]
        The size of the party

    {{prop}} id [int]
        The ID of the party

    {{prop}} size [int]
        The size of the party
    """
    def __init__(self, *, id, size):
        self.id = int(id)
        self.size = size

    def __dict__(self):
        """
        {{bltin}} instance.__dict__()
        {{usage}} dict(instance)

        {{pydesc}} __dict__

        {{rtn}} [dict] The send-ready object
        """
        return {"id": self.id, "size": self.size}
