__all__ = ["SemiStatus"]

class SemiStatus:
    def __init__(self, **kw):
        if kw:
            print(
                "Error: Class 'SemiStatus' has extra kwargs added by the gateway"
            )
            print(kw)
            exit()
