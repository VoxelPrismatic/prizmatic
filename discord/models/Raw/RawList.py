from .RawObjs import RawObjs

__all__ = ["RawList"]

class RawList:
    """
    {{cls}} instance = RawList(typ, url, bot, *a, **kw)

    {{desc}} Represents a list of RawObj objects, but is itself raw too! Useful
    for things that return a list that is online, like a list of reactions

    {{param}} typ [Class]
        The type of object to create

    {{param}} url [str]
        Where to download the list

    {{param}} bot [~/Bot]
        The bot object

    {{param}} *a, **kw [args, kwargs]
        How to initialize the objects in the list

    {{prop}} typ [Class]
        The type of object to create

    {{prop}} url [str]
        Where to download the object

    {{prop}} data [List[Any]]
        A list of fully created objects

    {{prop}} raw_data [List[~.RawObj]]
        A list of ~.RawObj s

    {{prop}} is_raw [bool, None]
        Whether or not the object is raw, `None` indicating that it hasn't been
        downloaded yet

    {{prop}} bot [~/Bot]
        The bot object

    {{prop}} a [List[Any]]
        A list of *args to initialize each object

    {{prop}} kw [Dict[Any: Any]]
        A dict of **kwargs to initialize each object
    """
    def __init__(self, typ, url, bot = None, *a, **kw):
        self.bot = bot
        if "bot_obj" in kw:
            self.bot = kw["bot_obj"]
        elif bot and "bot_obj" not in kw:
            kw["bot_obj"] = bot
        else:
            raise TypeError("The bot object was not found")
        self.url = url
        self.typ = typ
        self.raw_data = []
        self.data = []
        self.is_raw = None
        self.a = a
        self.kw = kw

    async def make(self):
        """
        {{fn}} await instance.make()

        {{desc}} Downloads the list and creates each item in that list

        {{rtn}} [List[Any]] The fully created list
        """
        if self.is_raw == None:
            await self.raw()
            self.data = self.data.make()
        if self.raw == True:
            self.data = self.data.make()
        self.is_raw = False
        return self.data

    async def raw(self):
        """
        {{fn}} await instance.raw()

        {{desc}} Downloads the list but each item in that list is raw

        {{rtn}} [List[~.RawObj]] The list of raw objects
        """
        if self.is_raw == None:
            data = await self.bot.http.req(u = self.url)
            self.data = RawObjs(self.typ, data, *self.a, **self.kw)
            self.raw_data = self.data
            self.is_raw = True
        return self.raw_data

    async def update(self):
        """
        {{fn}} await instance.update()

        {{desc}} Re-downloads the list as a raw list

        {{rtn}} [List[~.RawObj]] The list of raw objects
        """
        self.is_raw = None
        return await self.raw()

    async def remake(self):
        """
        {{fn}} await instance.remake()

        {{desc}} Re-downloads the list as a completely made list

        {{rtn}} [List[Any]] A list of fully created objects
        """
        self.is_raw = None
        return await self.make()

    def __call__(self):
        """
        {{bltin}} instance.__call__()
        {{usage}} instance()

        {{desc}} Short-hand for `instance.objs` or `instance.raw_objs` for lazy
        people like me

        {{rtn}} [bytes] The bytes object
        """
        if self.is_raw:
            return self.raw_objs
        return self.objs

    def __repr__(self):
        """
        {{bltin}} instance.__repr__()
        {{usage}} repr(instance)

        {{pydesc}} __repr__

        {{rtn}} [str]
        """
        if self.is_raw == None:
            status = "empty"
        elif self.is_raw == True:
            status = "raw"
        else:
            status = "created"
        return f"<RawList of {self.url} // Is currently {status}>"

    def __getitem__(self, index: int):
        """
        {{bltin}} instance.__getitem__(index)
        {{usage}} instance[index]

        {{param}} index [int]
            The index to get

        {{desc}} Returns a raw object if `instance.is_raw` is `True`, otherwise
        it returns an actual object

        {{rtn}} [Any] The corrosponding object
        """
        if self.is_raw:
            return self.raw_objs[index]
        return self.objs[index]

    def __setitem__(self, index: int, value):
        """
        {{bltin}} instance.__setitem__(index, value)
        {{usage}} instance[index] = value

        {{pydesc}} __setitemL__

        {{param}} index [int]
            The index to edit

        {{param}} value [Any]
            The value to set to

        {{note}} All changes will be erased upon calling any of `raw()`,
        `make()`, `update(), or `remake()` functions
        """
        self.data[index] = value
        self.raw_data[index] = value

    def __delitem__(self, index):
        """
        {{bltin}} instance.__delitem__(index)
        {{usage}} del instance[index]

        {{param}} index [int]
            The index to delete

        {{note}} Just like above, all changes will be erased upon calling any
        of those functions
        """
        del self.data[index]
        del self.raw_data[index]
