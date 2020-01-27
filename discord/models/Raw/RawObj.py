__all__ = ["RawObj"]

class RawObj:
    """
    {{cls}} instance = RawObj(typ, *args, **kwargs)

    {{desc}} Represents an object that hasn't actually been created yet, but
    unlike the regular Raw, this class already has all the info needed to make
    the object.

    {{param}} typ [Class]
        The type of object to create

    {{param}} *args, **kwargs [args, kwargs]
        How to initialize the object

    {{prop}} typ [Class]
        The type of object to create

    {{prop}} args [List[Any]]
        A list of *args to initialize the object

    {{prop}} kw [Dict[Any: Any]]
        A dict of **kwargs to initialize the object

    {{prop}} obj [Any]
        The actual object

    {{note}} Any attributes from the kwargs are also set as attributes within
    the class
    """
    def __init__(self, typ, *args, **kwargs):
        self.typ = typ
        self.args = args
        self.kw = kwargs
        self.obj = None
        for attr in kwargs:
            self.__setattr__(attr, kwargs[attr])

    def make(self):
        """
        {{fn}} instance.make()

        {{desc}} Actually makes the object

        {{rtn}} [Any] The created object
        """
        if not self.obj:
            self.obj = self.typ(*self.args, **self.kw)
        return self.obj

    def __call__(self):
        """
        {{bltin}} instance.__call__()
        {{usage}} instance()

        {{desc}} Short-hand for `instance.obj` for lazy people like me

        {{rtn}} [bytes] The bytes object
        """
        return self.obj

    def __repr__(self):
        """
        {{bltin}} instance.__repr__()
        {{usage}} repr(instance)

        {{pydesc}} __repr__

        {{rtn}} [str]
        """
        maybe = ' not' if not self.obj else ''
        return f"<RawObj of {self.typ} // Has{maybe} been created>"
