class NonExistentObj:
    """
    DESCRIPTION ---
        Used for objects that have been deleted, useful for recreating
        objects to get around Discord's no recreation policy.
    
    PARAMS ---
        url [str]
        - Where to post the data
        
        typ [class]
        - The object to recreate
        
        bot [Bot]
        - The bot object
        
        data [dict]
        - Params to recreate the object
        
        edit [dict]
        - How to edit the object after creation
    
    FUNCTIONS ---
        deleted_obj = NonExistentObj(url, bot, **kw)
        - Creates a new NonExistentObj object
        
        await deleted_obj.undelete()
        - Undelete the object. However, if it is a channel, the messages will not
          come back. This actually does recreate the object on Discord's end.
    """
    def __init__(self, url, typ, bot, data = {}, edit = {}):
        self.url = url
        self.typ = typ
        self.bot = bot
        self.dat = data
        self.edt = edit
    
    async def undelete(self):
        o = self.bot.http.req(m = "+", u = self.url, d = self.dat)
        obj = self.typ(**o)
        if self.edt != {}:
            await obj.edit(**self.edt)
        return obj
