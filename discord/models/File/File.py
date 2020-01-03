import random
from ..Error import ClassError
import re
import io
from ..Raw import RawFile, RawData
import aiohttp
import aiofiles

__all__ = ["rand_name", "File"]

def rand_name():
    return "".join(random.choice("0123456789ABCDEF") for x in range(16))

class File:
    """
    {{cls}} instance = File(obj, [name])

    {{desc}} Represnts a file, used for sending files in messages

    {{param}} obj [str, bytes, file, RawFile, RawData]
        Just some way to get file data

    {{param}} name [str]
        The name of the file
        {{norm}} Random hex

    {{prop}} data [~/Raw.RawFile]
        The file data

    {{prop}} name [str]
        Name of the file
    """
    def __init__(self, obj, name = rand_name()):
        self.name = name
        if type(obj) == str:
            if re.search(r"^https?://.+\..+$", obj):
                self.data = RawFile(obj)
            else:
                self.data = RawData(bytes(open(obj, "rb").read()))
        elif type(obj) == bytes:
            self.data = RawData(obj)
        elif type(obj) == io.IOBase:
            self.data = RawData(bytes(obj.read()))
        elif type(obj) == RawData or type(obj) == RawFile:
            self.data = obj
        else:
            raise ClassError(
                obj, RawData, [str, bytes, io.IOBase, RawFile, RawData, "url"]
            )

    async def get(self):
        """
        {{fn}} await instance.get()

        {{desc}} Gets the data if it was from a URL

        {{rtn}} [bytes] The data
        """
        return await self.data.get()

    async def send(self, index = ""):
        """
        {{fn}} await instance.send()

        {{pydesc}} __dict__

        {{rtn}} [dict]
        """
        return {
            "name": "file" + str(index),
            "value": await self.get(),
            "filename": self.name,
            "content_type": "application/octet-stream"
        }
