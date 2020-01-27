from .RawObj import RawObj
from ..Error import ClassError

__all__ = ["RawObjs"]

class RawObjs:
    """
    {{cls}} instance = RawObjs(type, ls, *args, **kwargss)

    {{desc}} Makes a list of RawObj objects from a list and a class

    {{param}} typ [Class]
        The type of object to create

    {{param}} ls [List[dict]]
        A list of objects sent from discord

    {{param}} *args, **kwargs [args, kwargs]
        Global args and kwargs for each object's initialization

    {{prop}} ls [List[dict]]
        A list of objects sent from discord

    {{prop}} typ [Class]
        The type of object to create

    {{prop}} data [List[Any]]
        The actual objects

    {{prop}} raw_data [List[~.RawObj]]
        A list of raw objects

    {{prop}} is_raw [bool, None]
        Whether or not it is raw, `None` denoting that it has not been created
        yet
    """
    def __init__(self, typ, ls, *args, **kwargs):
        for i in range(len(ls)):
            ls[i].update(kwargs)
        self.ls = ls
        self.typ = typ
        self.data = []
        self.arg = args
        self.raw_data = []
        self.is_raw = None

    def make(self):
        if self.raw == None:
            self.data = [self.typ(*self.arg, **kw) for kw in self.ls]
            self.raw()
        elif self.raw == True:
            self.data = [thing.make() for thing in self.raw_data]
        self.raw = False
        return self.objs

    def raw(self):
        if self.raw == None:
            self.raw_data = [
                RawObj(self.typ, *self.args, **kw) for kw in self.ls
            ]
            self.data = self.raw_data
            self.is_raw = True
        return self.raw_data

    def __call__(self):
        """
        {{bltin}} instance.__call__()
        {{usage}} instance()

        {{desc}} Short-hand for `instance.data` for lazy people like me

        {{rtn}} [bytes] The bytes object
        """
        return self.objs

    def __getitem__(self, index: int):
        """
        {{bltin}} instance.__getitem__(index)
        {{usage}} instance[index]

        {{pydesc}} __getitemL__

        {{param}} index [int]
            The index of the object

        {{rtn}} [Any] The corrosponding object
        """
        if self.is_raw:
            return self.raw_data[index]
        return self.data[index]

    def __delitem__(self, index):
        """
        {{bltin}} instance.__delitem__(index)
        {{usage}} del instance[index]

        {{pydesc}} __delitemL__

        {{param}} index [int]
            The index of the object
        """
        try:
            del self.data[index]
        except IndexError:
            pass
        try:
            del self.raw_data[index]
        except IndexError:
            pass
        del self.ls[index]

    def __setitem__(self, i, val):
        """
        {{bltin}} instance.__setitem__(i, val)
        {{usage}} instance[i] = val

        {{pydesc}} __setitemL__

        {{param}} i [int]
            The index of the object

        {{param}} val [Any]
            The value of the object
        """
        if type(val) == RawObj:
            self.ls[i] = val.kw
        elif type(val) == dict:
            self.ls[i] = val
        elif type(val) == self.typ:
            self.ls[i] = dict(val)
        else:
            raise ClassError(val, self.typ, [RawObj, dict, self.typ])
        if self.raw == True:
            self.is_raw = None
            self.raw()
        elif self.raw == False:
            self.is_raw = None
            self.make()

    def __repr__(self):
        """
        {{bltin}} instance.__repr__()
        {{usage}} repr(instance)

        {{pydesc}} __repr__

        {{rtn}} [str]
        """
        if self.raw == None:
            status = "empty"
        elif self.raw == True:
            status = "raw"
        else:
            status = "created"
        return f"<RawObjs of {self.typ} // Is currently {status}>"
