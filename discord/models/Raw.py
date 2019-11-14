import io
import aiohttp

class Raw:
    """
    DESCRIPTION ---
        Represents an object that hasn't actually been created yet via URL,
        useful for objects that shouldn't have any infinite recursions
        or if it would take too long to grab an object immediately.
        
    PARAMS ---
        id [int]
        - The ID of the object
        
        url [str]
        - The URL of where to get this data
        
        typ [Class]
        - The object to be created
        
        bot [Bot]
        - The bot object
        
        **fmt [any]
        - How to format the URL, not needed tho
        - Is just `url.format(**fmt)', so do what you want with that
        - NOTE: The `id' kwarg is autofilled
        
    FUNCTIONS ---
        thing = Raw(id, url, typ, bot, **fmt)
        - Create a Raw object
        
        await thing.get()
        - Generate the object and return it, must be awaited or it
          will not work
        - Will return the object if it has already been generated
        
        await thing.update()
        - Updates the object via the URL
        
        thing()
        - Returns the object as is
    """
    def __init__(self, id, url, typ, bot, **fmt):
        self.id = int(id)
        self.typ = typ
        self.bot = bot
        fmt["id"] = id
        self.url = url.format(**fmt)
        self.obj = None
    async def get(self):
        if not obj:
            kw = await self.bot._http(u = self.url)
            self.obj = self.typ(**kw)
        return self.obj
    
    async def update(self):
        self.obj = None
        return await self.get()
    
    def __call__(self):
        return self.obj
        
    def __repr__(self):
        return f"<Raw of {self.typ} // Has{' not' if not self.obj else ''} been created>"

class RawFile:
    """
    DESCRIPTION ---
        Represents a file that is awaiting a download
        
    PARAMS ---
        url [str]
        - The url to download
        
    FUNCTIONS ---
        thing = RawFile(url)
        - Creates a new RawFile object
        
        await thing.get()
        - Download the file, returns the BytesIO object
        - If already downloaded, just return the file
        
        thing()
        - Returns the BytesIO object as is
    """
    def __init__(self, url):
        self.url = url
        self.downloaded = False
        self.data = io.BytesIO()
    
    async def get(self):
        if not self.downloaded:
            async with asyncio.ClientSession() as c:
                async with c.get(self.url) as r:
                    self.data = io.BytesIO(await r.read())
            self.downloaded = True
        return self.data
    
    def __call__(self):
        return self.data
    
    def __repr__(self):
        return f"<RawFile of {self.url} // Has{' not' if not self.downloaded else ''} been downloaded>"

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
            self.obj = self.typ(*args, **kwargs)
        return self.obj
    
    def __call__(self):
        return self.obj
        
    def __repr__(self):
        return f"<RawObj of {self.typ} // Has{' not' if not self.obj else ''} been created>"
        
class RawList:
    """
    DESCRIPTION ---
        Represents a list of RawObj objects, but is itself raw too!
        Useful for things that return a list of things that you want to be raw.
        
    PARAMS ---
        typ [Class]
        - The object to create
        
        url [str]
        - Where to get the data from
        
        bot [Bot]
        - The bot object
        
    FUNCTIONS ---
        thing = RawList(url)
        - Creates a new RawList object
        
        await thing.make()
        - Gets all objects and returns them
        
        await thing.raw()
        - Returns the list of RawObj objects
        
        await thing.update()
        - Updates all data, and returns the list of RawObj objects
        
        await thing.remake()
        - Updates all data, and returns the list of actual objects
        
        thing()
        - Returns the list as is
    """
    def __init__(self, typ, url, bot):
        self.bot = bot
        self.url = url
        self.typ = typ
        self.raw_data = []
        self.data = []
        self.raw = None
    
    async def make(self):
        if self.raw == None:
            data = await self.bot._http(u = self.url)
            self.data = [self.typ(**data[kw]) for kw in data]
            if self.raw_data == []:
                self.raw_data = [RawObj(self.typ, **data[kw]) for kw in data]
        if self.raw == True:
            self.data = [obj.make() for obj in self.data]
        self.raw = False
        return self.data
    
    async def raw(self):
        if self.raw == None:
            data = await self.bot._http(u = self.url)
            self.data = [RawObj(self.typ, **data[kw]) for kw in data]
            self.raw_data = self.data
            raw = True
        return self.raw_data
    
    async def update(self):
        self.raw = None
        return await self.raw()
    
    async def remake(self):
        self.raw = None
        return await self.make()
        
    def __call__(self):
        return self.data
        
    def __repr__(self):
        if self.raw == None:
            status = "empty"
        elif self.raw == True:
            status = "raw"
        else:
            status = "created"
        return f"<RawList of {self.url} // Is currently {status}>"
    