__all__ = ["SemiInvite"]

class SemiInvite:
    def __init__(self, **kw):
        if kw:
            print(
                "Error: Class 'SemiInvite' has extra kwargs added by the gateway"
            )
            print(kw)
            exit()
