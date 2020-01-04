__all__ = ["SemiGuild"]

class SemiGuild:
    def __init__(self, **kw):
        if kw:
            print(
                "Error: Class 'SemiGuild' has extra kwargs added by the gateway"
            )
            print(kw)
            exit()
