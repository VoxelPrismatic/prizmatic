__all__ = ["VoiceClient"]

class VoiceClient:
    """
    {{cls}} instance = VoiceClient()

    {{desc}} Allows connecting to voice channels

    {{note}} This class doesn' actually exist yet
    """
    def __init__(self, *a, **kw):
        if kw or a:
            print(
                "Error: Class 'VoiceClient' has extra kwargs added by the gateway"
            )
            print(kw, a)
            exit()
