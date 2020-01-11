import io
import aiohttp

__all__ = ["Raw"]

class Raw:
    """
    {{cls}} instance = Raw()

    {{desc}} Represents an object that hasn't actually been created yet via URL,
    useful for objects that shouldn't have any infinite recursions or if it
    would take too long to grab an object normally.

    {{note}} Documentation for this class is not complete yet
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
