__all__ = ["SemiInvite"]

class SemiInvite:
    """
    {{cls}} instance = SemiInvite()

    {{desc}} Represents an invite with incomplete data

    {{note}} Documentation for this class is not complete yet
    """
    def __init__(self, **kw):
        if kw:
            print(
                "Error: Class 'SemiInvite' has extra kwargs added by the gateway"
            )
            print(kw)
            exit()
