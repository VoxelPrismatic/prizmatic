import io
import aiohttp

__all__ = ["Raw"]

class Raw:
    """
    {{cls}} instance = Raw(typ, id, bot, **fmt)

    {{desc}} Represents an object that hasn't actually been created yet via URL,
    useful for objects that shouldn't have any infinite recursions or if it
    would take too long to grab an object normally.

    {{param}} typ [Class]
        The type of object to create

    {{param}} id [int]
        ID of the object to create

    {{param}} url [str]
        Where to download the object from

    {{param}} bot [~/Bot]
        The bot object

    {{param}} **fmt [kwargs]
        How to format the URL if necessary, ID is included automatically

    {{prop}} id [int]
        ID of the object

    {{prop}} typ [Class]
        The type of object to create

    {{prop}} url [str]
        Where to download the object from

    {{prop}} bot [~/Bot]
        The bot object

    {{prop}} fmt [dict]
        The formatting

    {{prop}} obj [Any]
        The actual object
    """
    def __init__(self, typ, id, url, bot, **fmt):
        self.id = int(id)
        self.typ = typ
        self.bot = bot
        fmt["id"] = id
        self.url = url.format(**fmt)
        self.obj = None

    async def get(self):
        """
        {{fn}} await instance.get()

        {{desc}} Downloads the object

        {{rtn}} [Any] The downloaded object
        """
        if not self.obj:
            kw = await self.bot._http(u = self.url)
            self.obj = self.typ(bot_obj = self.bot, **kw)
        return self.obj

    async def update(self):
        """
        {{fn}} await instance.update()

        {{desc}} Re-downloads the object

        {{rtn}} [Any] The downloaded object
        """
        self.obj = None
        return await self.get()

    def __call__(self):
        """
        {{bltin}} instance.__call__()
        {{usage}} instance()

        {{desc}} Short-hand for `instance.obj` for lazy people like me

        {{rtn}} [Any] The downloaded object
        """
        return self.obj

    def __repr__(self):
        """
        {{bltin}} instance.__repr__()
        {{usage}} repr(instance)

        {{pydesc}} __repr__

        {{rtn}} [str]
        """
        maybe = ' not' if not self.obj else ''
        return f"<Raw of {self.typ} // Has{maybe} been created>"
