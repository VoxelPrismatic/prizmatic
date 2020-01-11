__all__ = ["SemiGuild"]

class SemiGuild:
    """
    {{cls}} instance = SemiGuild()

    {{desc}} Represents a guild with incomplete data

    {{note}} Documentation for this class is not complete yet
    """
    def __init__(self, **kw):
        if kw:
            print(
                "Error: Class 'SemiGuild' has extra kwargs added by the gateway"
            )
            print(kw)
            exit()
