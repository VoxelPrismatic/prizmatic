__all__ = ["SemiVoiceState"]

class SemiVoiceState:
    def __init__(self, **kw):
        if kw:
            print(
                "Error: Class 'SemiVoiceState' has extra kwargs added by the gateway"
            )
            print(kw)
            exit()
