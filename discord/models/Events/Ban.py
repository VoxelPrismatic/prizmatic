from ..ClsUtil import extra_kw

__all__ = ["Ban"]

class Ban:
    """
    {{cls}} instance = Ban()

    {{desc}} Represents a ban

    {{noexist}}
    """
    def __init__(self, **kw):
        extra_kw(kw, "Ban")
