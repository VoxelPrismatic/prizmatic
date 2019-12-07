from ..Bot import Bot

__all__ = ["RawAny"]

class RawAny:
    """
    DESCRIPTION ---
        Acts like a raw object, until it's created. When it is created, it turns
        into the object you wanted.

    PARAMS ---
        typ [type]
        - What to initialize, should be from this class

        url [str]
        - The url, like in Raw

        bot [Bot]
        - The bot object, so this class can be transformed properly

        *a, **kw
        - Other args to initialize with

    FUNCTIONS ---
        raw_any = RawAny(typ, url, bot)
        - Create a new RawAny object

        await raw_any.make()
        - The magical transformation function
    """
    def __init__(self, typ, url, bot = None, *a, **kw):
        if type(bot) != Bot and "bot_obj" not in kw:
            raise TypeError("Could not find bot object explicitly or as 'bot_obj' in kw")
        self.typ = typ
        self.url = url
        self.a = a
        self.kw = kw
        self.bot = bot

    async def make(self):
        d = await self.bot.http.req(u = self.url)
        o = self.typ(*self.a, **self.kw, **d)
        del self.url
        del self.a
        del self.kw
        del self.typ
        self = o
