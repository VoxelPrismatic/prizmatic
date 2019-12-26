__all__ = ["NonExistentObj"]

class NonExistentObj:
    """
    {{cls}} instance = NonExistentObj(url, typ, bot, data, edit)

    {{desc}} Used for objects that have been deleted, useful for recreating
    objects to get around Discord's no recreation policy. Basically, this is an
    undo button

    {{note}} This class shouldn't be initialized by hand as it doesn't do
    anything too useful. This object is automatically initialized upon an
    object's `delete()` call.

    {{note}} Due to the nature of Discord's policy, ID and messages CANNOT be
    restored.

    {{param}} url [str]
        Where to post the data

    {{param}} typ [class]
        The object to recreate, eg Text or Channel. This param is only used to
        recreate the object before it was deleted.

    {{param}} bot [discord.Bot]
        The bot object

    {{param}} data [dict]
        Params to recreate the object. This is used for simple params on
        creation like name or position

    {{param}} edit [dict]
        How to edit the object after creation

    {{param}} extras [list]
        Other requests to edit, used in the format [http_method, url, data]. The
        data MUST be a dict.

    {{prop}} url [str]
        The URL provided

    {{prop}} typ [class]
        The object's class

    {{prop}} bot [discord.Bot]
        The bot object

    {{prop}} dat [dict]
        Initial creation params

    {{prop}} edt [dict]
        Post creation params

    {{prop}} ext [list]
        Provided extras
    """
    def __init__(self, url, typ, bot, data: dict = {}, edit = {}, extras = []):
        self.url = url
        self.typ = typ
        self.bot = bot
        self.dat = data
        self.edt = edit
        self.ext = extras

    async def undelete(self):
        """
        {{fn}} await instance.undelete()

        {{desc}} Recreates the object that was deleted. This process is not
        perfect, however.

        {{note}} Here are the things that CANNOT be restored: IDs, messages,
        members, the roles that members have, the members that a role has, roles
        upon a guild's creation, etc. If you must recreate those, use the extras
        upon initialization.

        {{rtn}} The recreated object
        """
        o = await self.bot.http.req(m = "+", u = self.url, d = self.dat)
        obj = self.typ(**o)
        if self.ext != []:
            for meth, url, data in self.extras:
                await self.bot.http.req(m = meth, u = url, d = data)
        if self.edt != {}:
            await obj.edit(**self.edt)
        return obj
