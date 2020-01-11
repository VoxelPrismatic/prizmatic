__all__ = ["SemiIntegration"]

class SemiIntegration:
    """
    {{cls}} instance = SemiIntegration(*, id, name, type, account, bot_obj)

    {{desc}} Represents a partial integration

    {{note}} Documentation for this class is not complete yet
    """
    def __init__(self, *, id, name, type, account, bot_obj):
        self.id = int(id)
        self.name = name
        self.type = type
        self.account = account
        self.bot_obj = bot_obj

    @property
    def acc(self):
        return self.account
