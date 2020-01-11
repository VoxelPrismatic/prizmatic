from ..Bot import Bot

__all__ = ["RawAny"]

class RawAny:
    """
    {{cls}} instance = RawAny()

    {{desc}} Acts like a raw object, until it's created. When it is created, it
    turns into the object you wanted.

    {{note}} Documentation for this class is not complete yet
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
