__all__ = ["RawAny"]

class RawAny:
    """
    {{cls}} instance = RawAny(typ, url, bot, *a, **kw)

    {{desc}} Acts like a raw object, until it's created. When it is created, it
    turns into the object you wanted.

    {{param}} typ [Class]
        The type of object to create

    {{param}} url [str]
        Where to download the object

    {{param}} bot [~/Bot]
        The bot object

    {{param}} *a, **kw [args, kwargs]
        How to initialize the object

    {{prop}} typ [Class]
        The type of object to create

    {{prop}} url [str]
        Where to download the object

    {{prop}} a [List[Any]]
        A list of *args for the object's initialization

    {{prop}} kw [Dict[Any: Any]]
        A dict of **kwargs for the object's initialization

    {{prop}} bot [~/Bot]
        The bot object
    """
    def __init__(self, typ, url, bot = None, *a, **kw):
        if bot is None and "bot_obj" not in kw:
            raise TypeError(
                "Could not find bot object explicitly or as 'bot_obj' in kw"
            )
        self.typ = typ
        self.url = url
        self.a = a
        self.kw = kw
        self.bot = bot

    async def make(self):
        """
        {{fn}} await instance.make()

        {{desc}} The transformation shall commense

        {{rtn}} [Any] The created object
        """
        d = await self.bot.http.req(u = self.url)
        o = self.typ(*self.a, **self.kw, **d)
        del self.url
        del self.a
        del self.kw
        del self.typ
        self = o
        return self
