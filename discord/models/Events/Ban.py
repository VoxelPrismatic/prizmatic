from ..ClsUtil import extra_kw

__all__ = ["Ban"]

class Ban:
    """
    {{cls}} instance = Ban()

    {{desc}} Represents a ban

    {{note}} This class doesn't actually exist yet
    """
    def __init__(self, **kw):
        extra_kw(kw, "Ban")
