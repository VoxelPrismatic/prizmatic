import io
import aiohttp

__all__ = ["RawFile"]

class RawFile:
    """
    {{cls}} instance = RawFile()

    {{desc}} Represents a file that is awaiting a download

    {{note}} Documentation for this class is not complete yet
    """
    def __init__(self, url, data = {}):
        self.url = url
        self.downloaded = False
        self.data = io.BytesIO()

    async def get(self):
        if not self.downloaded:
            async with aiohttp.ClientSession() as c:
                async with c.get(self.url) as r:
                    self.data = io.BytesIO(await r.read())
            self.downloaded = True
        return self.data

    def __call__(self):
        return self.data

    def __repr__(self):
        tmp = ' not' if not self.downloaded else ''
        return f"<RawFile of {self.url} // Has{tmp} been downloaded>"

    async def update(self):
        self.downloaded = False
        return await self.get()
