__all__ = ["SemiStatus"]

class SemiStatus:
    """
    {{cls}} instance = SemiStatus()

    {{desc}} Represents a status with incomplete data

    {{note}} Documentation for this class is not complete yet
    """
    def __init__(self, **kw):
        if kw:
            print(
                "Error: Class 'SemiStatus' has extra kwargs added by the gateway"
            )
            print(kw)
            exit()
