__all__ = ["SemiVoiceState"]

class SemiVoiceState:
    """
    {{cls}} instance = SemiVoiceState()

    {{desc}} Represents a voice status with incomplete data

    {{note}} Documentation for this class is not complete yet
    """
    def __init__(self, **kw):
        if kw:
            print(
                "Error: Class 'SemiVoiceState' has extra kwargs added by the gateway"
            )
            print(kw)
            exit()
