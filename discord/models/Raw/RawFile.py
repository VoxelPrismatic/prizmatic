import io
import aiohttp

__all__ = ["RawFile"]

class RawFile:
    """
    {{cls}} instance = RawFile(url)

    {{desc}} Represents a file that is awaiting a download

    {{param}} url [str]
        Where to download the file

    {{prop}} url [str]
        Where to download the file

    {{prop}} downloaded [bool]
        Whether or not the file has been downloaded

    {{prop}} data [io.BytesIO]
        The file object
    """
    def __init__(self, url):
        self.url = url
        self.downloaded = False
        self.data = io.BytesIO()

    async def get(self):
        """
        {{fn}} await instance.get()

        {{desc}} Downloads the file

        {{rtn}} [io.BytesIO] The downloaded file
        """
        if not self.downloaded:
            async with aiohttp.ClientSession(timeout = 60) as c:
                async with c.get(self.url) as r:
                    self.data = io.BytesIO(await r.read())
            self.downloaded = True
        return self.data

    def __call__(self):
        """
        {{bltin}} instance.__call__()
        {{usage}} instance()

        {{desc}} Short-hand for `instance.data` for lazy people like me

        {{rtn}} [bytes] The bytes object
        """
        return self.data

    def __repr__(self):
        """
        {{bltin}} instance.__repr__()
        {{usage}} repr(instance)

        {{pydesc}} __repr__

        {{rtn}} [str]
        """
        tmp = ' not' if not self.downloaded else ''
        return f"<RawFile of {self.url} // Has{tmp} been downloaded>"

    async def update(self):
        """
        {{fn}} await instance.update()

        {{desc}} Re-downloads the file

        {{rtn}} [io.BytesIO] The downloaded file
        """
        self.downloaded = False
        return await self.get()
