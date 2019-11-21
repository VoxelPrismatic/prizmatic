import io
import aiohttp

class Raw:
    """
    DESCRIPTION ---
        Represents  an object that  hasn't  actually been  created yet  via URL,
        useful for  objects that shouldn't have any infinite recursions or if it 
        would    take    too    long    to     grab    an    object    normally.

        NOTE: If  you  want to  make a class  that says  not to, it  is OKAY  to 
              initialize that class in this way. However, it will not be able to
              be  located in any  part of this module  unless you use this line:
              `bot.listeners.<type eg 'channels'>[<id>] = obj`

              If you want to make a class using URLs, use the following instead:
              `await bot.make(<type eg 'channels'>, <id>, <url>)`
              
              Types: Channels
        
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
    def __init__(self, typ, id, url, bot, **fmt):
        self.id = int(id)
        self.typ = typ
        self.bot = bot
        fmt["id"] = id
        self.url = url.format(**fmt)
        self.obj = None
    async def get(self):
        if not self.obj:
            kw = await self.bot._http(u = self.url)
            self.obj = self.typ(bot_obj = self.bot, **kw)
        return self.obj
    
    async def update(self):
        self.obj = None
        return await self.get()
    
    def __call__(self):
        return self.obj
        
    def __repr__(self):
        return f"<Raw of {self.typ} // Has{' not' if not self.obj else ''} been created>"