__all__ = ["SemiUser"]

class SemiUser:
    def __init__(self, **kw):
        if kw:
            print(
                "Error: Class 'SemiUser' has extra kwargs added by the gateway"
            )
            print(kw)
            exit()
