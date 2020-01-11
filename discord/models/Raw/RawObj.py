__all__ = ["RawObj"]

class RawObj:
    """
    {{cls}} instance = RawObj()

    {{desc}} Represents an object that hasn't actually been created yet, but
    unlike the regular Raw, this class already has all the info needed to make
    the object.

    {{note}} Documentation for this class is not complete yet
    """
    def __init__(self, typ, *args, **kwargs):
        self.typ = typ
        self.args = args
        self.kw = kwargs
        self.obj = None

    def make(self):
        if not self.obj:
            self.obj = self.typ(*self.args, **self.kw)
        return self.obj

    def __call__(self):
        return self.obj

    def __repr__(self):
        return f"<RawObj of {self.typ} // Has{' not' if not self.obj else ''} been created>"
