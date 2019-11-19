from .RawObj import RawObj
from ..Error import ClassError

class RawObjs:
    """
    DESCRIPTION ---
        Makes a list of RawObj objects from a list and a class
    
    PARAMS ---
        typ [Class]
        - The object to create
        
        ls [list(obj)]
        - The params of the objects
        
        *args, **kwargs
        - Universal parameters
        
    FUNCTIONS ---
        raw_objs = RawObjs(typ, ls)
        - Create a RawObjs object
        
        raw_objs.make()
        - Create all objects fully, and return it
        
        raw_objs.raw()
        - Create only RawObj objects, and return it
        
        raw_objs()
        - Return the current list of objects
        
        raw_objs[index]
        - Return the object at that index
        
        raw_objs[index] = val
        - Set that index to val, effects everything
        
        del raw_objs[index]
        - Delete that item, effects everything
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
            self.raw_data = [RawObj(self.typ, *self.args, **kw) for kw in self.ls]
            self.data = self.raw_data
            self.is_raw = True
        return self.raw_data
    
    def __call__(self):
        return self.objs
    
    def __getitem__(self, index):
        return self.data[index]
    
    def __delitem__(self, index):
        del self.data[index]
        del self.raw_data[index]
        del self.ls[index]
    
    def __setitem__(self, i, val):
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
        if self.raw == None:
            status = "empty"
        elif self.raw == True:
            status = "raw"
        else:
            status = "created"
        return f"<RawObjs of {self.typ} // Is currently {status}>"