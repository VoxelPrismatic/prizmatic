__all__ = ["RawObj"]

class RawObj:
    """
    DESCRIPTION ---
        Represents an object that hasn't actually been created yet,
        but unlike the regular Raw, this class already has all the
        info needed to make the object.

    PARAMS ---
        typ [Class]
        - The object to create

        *args, **kwargs
        - As if you were to create the object

    FUNCTIONS ---
        thing = RawObj(typ, *args, **kwargs)
        - Creates a new RawObj object

        thing.make()
        - Makes the object and returns it
        - Returns the created object if it is already made

        thing()
        - Returns the object
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
