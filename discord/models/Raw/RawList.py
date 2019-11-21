from .RawObjs import RawObjs

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
        
        data [dict]
        - Other data to be sent
        
        bot [Bot]
        - The bot object
        
        **uni
        - Universal kwargs
        
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
        
        thing[i], thing[i] = v, del thing[i]
        - Interact like a list
        - All changes will be deleted when using the update or remake 
          functions
    """
    def __init__(self, typ, url, data: dict = {}, bot = None, **uni):
        self.bot = bot
        if "bot_obj" in uni:
            self.bot = uni["bot_obj"]
        if bot and "bot_obj" not in uni:
            uni["bot_obj"] = bot
        self.url = url
        self.typ = typ
        self.kw = data
        self.raw_data = []
        self.data = []
        self.is_raw = None
        self.uni = uni
    
    async def make(self):
        if self.raw == None:
            await self.raw()
            self.data = self.data.make()
        if self.raw == True:
            self.data = self.data.make()
        self.is_raw = False
        return self.data
    
    async def raw(self):
        if self.raw == None:
            data = await self.bot.http.req(u = self.url)
            self.data = RawObjs(self.typ, data, **self.uni)
            self.raw_data = self.data
            self.is_raw = True
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
        if self.is_raw == None:
            status = "empty"
        elif self.is_raw == True:
            status = "raw"
        else:
            status = "created"
        return f"<RawList of {self.url} // Is currently {status}>"
    
    def __getitem__(self, i):
        try:
            return self.data[i]
        except IndexError:
            return self.raw_data[i]
    
    def __setitem__(self, i, v):
        self.data[i] = v
        self.raw_data[i] = v
    
    def __delitem__(self, i):
        del self.data[i]
        del self.raw_data[i]