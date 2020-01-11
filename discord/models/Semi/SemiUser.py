__all__ = ["SemiUser"]

class SemiUser:
    """
    {{cls}} instance = SemiUser()

    {{desc}} Represents a user with incomplete data

    {{note}} Documentation for this class is not complete yet
    """
    def __init__(self, **kw):
        if kw:
            print(
                "Error: Class 'SemiUser' has extra kwargs added by the gateway"
            )
            print(kw)
            exit()
